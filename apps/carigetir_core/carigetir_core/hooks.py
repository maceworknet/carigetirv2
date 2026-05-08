app_name = 'carigetir_core'
app_title = 'Carigetir Core'
app_publisher = 'CariGetir'
app_description = 'CariGetir V2 carigetir_core'
app_icon = 'octicon octicon-file-directory'
app_color = 'grey'
app_email = 'info@carigetir.com'
app_license = 'MIT'

scheduler_events = {
    "daily": [
        "carigetir_core.carigetir_core.utils.subscription.check_expired_subscriptions"
    ]
}
