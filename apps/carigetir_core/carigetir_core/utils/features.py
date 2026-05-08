import frappe

def get_current_company():
    """
    Returns the company associated with the currently logged-in user.
    """
    user = frappe.session.user
    if user == "Administrator":
        # For SaaS Super Admin, may need to handle differently or return a default
        pass
        
    company_user = frappe.db.get_value("CG Company User", {"user": user}, "company")
    return company_user

def is_subscription_active(company):
    """
    Checks if the given company has an active subscription.
    """
    if not company:
        return False
        
    subscription = frappe.get_doc("CG Subscription", {"company": company, "status": "Active"})
    if subscription and subscription.end_date >= frappe.utils.today():
        return True
    return False

def get_company_plan(company):
    """
    Retrieves the active plan for the given company.
    """
    if not company:
        return None
        
    subscription = frappe.db.get_value("CG Subscription", {"company": company, "status": "Active"}, "plan")
    return subscription

def get_enabled_features(company):
    """
    Returns a list of all feature keys enabled for the company.
    This includes features from the plan + feature overrides.
    """
    enabled_features = []
    
    plan = get_company_plan(company)
    if plan:
        # Get plan features
        plan_features = frappe.get_all("CG Plan Feature", filters={"parent": plan}, pluck="feature")
        for f in plan_features:
            feature_key = frappe.db.get_value("CG Feature", f, "feature_key")
            enabled_features.append(feature_key)
            
    # Check overrides
    overrides = frappe.get_all("CG Company Feature Override", filters={"company": company}, fields=["feature", "is_enabled"])
    for override in overrides:
        feature_key = frappe.db.get_value("CG Feature", override.feature, "feature_key")
        if override.is_enabled and feature_key not in enabled_features:
            enabled_features.append(feature_key)
        elif not override.is_enabled and feature_key in enabled_features:
            enabled_features.remove(feature_key)
            
    return enabled_features

def has_feature(company, feature_key):
    """
    Checks if a specific feature_key is enabled for the company.
    """
    if not company:
        return False
        
    if not is_subscription_active(company):
        return False
        
    enabled_features = get_enabled_features(company)
    return feature_key in enabled_features

def check_usage_limit(company, limit_key):
    """
    Checks if the company has reached its limit for a specific resource (users, branches, etc.).
    Returns (True, "Message") if limit exceeded, else (False, None).
    """
    plan = get_company_plan(company)
    if not plan:
        return True, "Aktif bir paket bulunamadı."
        
    plan_doc = frappe.get_doc("CG Plan", plan)
    
    # Example logic: limit_key = 'user_limit'
    limit_value = plan_doc.get(limit_key)
    
    if limit_value == 0: # 0 means unlimited
        return False, None
        
    # TODO: Calculate current usage based on limit_key and compare
    current_usage = 0 
    
    if current_usage >= limit_value:
        return True, f"{limit_key} limitine ulaşıldı. Lütfen paketinizi yükseltin."
        
    return False, None
