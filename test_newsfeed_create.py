from oxwall_site_model import OxwallSite
from value_models.status import Status


# TODO parametrize Status text
def test_add_text_status(driver, signed_in_user):
    status = Status(text="Shit happens!!!:(", user=signed_in_user)
    app = OxwallSite(driver)
    old_status_list = app.dash_page.status_list
    # Actions:
    app.dash_page.status_text_field.send_keys(status.text)
    app.dash_page.send_button.click()
    app.dash_page.wait_until_new_status_appeared()
    # Verification that new status with this text appeared
    new_status_list = app.dash_page.status_list
    assert len(new_status_list) == len(old_status_list) + 1
    new_status = new_status_list[0]
    assert status.text == new_status.text
    assert signed_in_user.real_name == new_status.user
    assert "within 1 minute" == new_status.time
