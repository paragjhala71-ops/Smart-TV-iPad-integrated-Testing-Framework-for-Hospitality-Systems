from state_engine import TVState, IPadState
from remote_module import RemoteControl
from ipad_module import IPadController
from validator import Validator


def test_switch_to_netflix():
    print("Running Test: Switch to Netflix")

    tv = TVState()
    ipad = IPadState()

    remote = RemoteControl(tv)
    ipad_controller = IPadController(tv, ipad)
    validator = Validator(tv, ipad)

    remote.power_on()
    remote.switch_module("Netflix")
    ipad_controller.sync_with_tv()

    result = validator.validate_sync()
    return result



def test_sync_failure():
    print("Running Test: Sync Failure Scenario")

    tv = TVState()
    ipad = IPadState()

    remote = RemoteControl(tv)
    validator = Validator(tv, ipad)

    remote.power_on()
    remote.switch_module("Netflix")

    # Intentionally NOT syncing iPad with TV
    # ipad_controller.sync_with_tv()  ← skipped on purpose

    result = validator.validate_sync()

    return result

def test_volume_increase():
    print("Running Test: Volume Increase")

    tv = TVState()
    ipad = IPadState()

    remote = RemoteControl(tv)

    remote.power_on()
    remote.volume_up()

    if tv.volume == 11:
        return "PASS"
    return "FAIL"