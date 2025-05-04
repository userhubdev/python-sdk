# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from ._checkout_cancel_step import CheckoutCancelStep
from ._checkout_complete_payment_step import CheckoutCompletePaymentStep
from ._checkout_trial_step import CheckoutTrialStep


@dataclasses.dataclass
class CheckoutStep:
    """
    The checkout step.
    """

    #: The type of step.
    type: str = ""
    #: The state of the step.
    state: str = ""
    #: The trial step details.
    trial: Optional[CheckoutTrialStep] = None
    #: The cancel step details.
    cancel: Optional[CheckoutCancelStep] = None
    #: The complete payment step details.
    complete_payment: Optional[CheckoutCompletePaymentStep] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.type is not None:
            data["type"] = self.type

        if self.state is not None:
            data["state"] = self.state

        if self.trial is not None:
            data["trial"] = CheckoutTrialStep.__json_encode__(self.trial)

        if self.cancel is not None:
            data["cancel"] = CheckoutCancelStep.__json_encode__(self.cancel)

        if self.complete_payment is not None:
            data["completePayment"] = CheckoutCompletePaymentStep.__json_encode__(
                self.complete_payment
            )

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CheckoutStep":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("trial") is not None:
            kwargs["trial"] = CheckoutTrialStep.__json_decode__(data["trial"])

        if data.get("cancel") is not None:
            kwargs["cancel"] = CheckoutCancelStep.__json_decode__(data["cancel"])

        if data.get("completePayment") is not None:
            kwargs["complete_payment"] = CheckoutCompletePaymentStep.__json_decode__(
                data["completePayment"]
            )

        return CheckoutStep(**kwargs)
