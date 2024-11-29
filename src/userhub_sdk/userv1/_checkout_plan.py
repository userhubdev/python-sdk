# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from userhub_sdk import commonv1

from ._checkout_plan_group import CheckoutPlanGroup
from ._checkout_plan_revision import CheckoutPlanRevision
from ._checkout_plan_savings import CheckoutPlanSavings
from ._checkout_plan_trial import CheckoutPlanTrial
from ._price import Price


@dataclasses.dataclass
class CheckoutPlan:
    """
    The plan.
    """

    #: The system-assigned identifier of the plan.
    id: str = ""
    #: The name of the plan.
    display_name: str = ""
    #: The description of the plan.
    description: Optional[str] = None
    #: The billing interval for the plan.
    billing_interval: commonv1.Interval = dataclasses.field(
        default_factory=commonv1.Interval
    )
    #: The plan group for the plan.
    group: CheckoutPlanGroup = dataclasses.field(default_factory=CheckoutPlanGroup)
    #: The revision for the plan.
    revision: CheckoutPlanRevision = dataclasses.field(
        default_factory=CheckoutPlanRevision
    )
    #: Whether this is the current plan for the subscription.
    current: Optional[bool] = None
    #: Whether this is the selected plan for the checkout.
    selected: Optional[bool] = None
    #: Whether this is the default plan for the plan group.
    default: Optional[bool] = None
    #: The trial settings.
    #:
    #: For authenticated requests, this will not be set when the account
    #: isn't eligible for a trial.
    trial: Optional[CheckoutPlanTrial] = None
    #: Whether the change is considered an upgrade or
    #: a downgrade.
    change_path: Optional[str] = None
    #: The flat price for the plan.
    #:
    #: This might not exists for plans that are billed by seat.
    price: Optional[Price] = None
    #: The primary seat price for the plan.
    seat_price: Optional[Price] = None
    #: The savings for the plan.
    #:
    #: The savings are in comparison to the plan in the revision with the
    #: shortest billing interval.
    savings: Optional[CheckoutPlanSavings] = None
    #: Whether this plan is disabled for checkout.
    #:
    #: This will only be set when the current/selected plan is disabled, all
    #: other plans will be available for checkout.
    disabled: Optional[bool] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.description is not None:
            data["description"] = self.description

        if self.billing_interval is not None:
            data["billingInterval"] = commonv1.Interval.__json_encode__(
                self.billing_interval
            )

        if self.group is not None:
            data["group"] = CheckoutPlanGroup.__json_encode__(self.group)

        if self.revision is not None:
            data["revision"] = CheckoutPlanRevision.__json_encode__(self.revision)

        if self.current is not None:
            data["current"] = self.current

        if self.selected is not None:
            data["selected"] = self.selected

        if self.default is not None:
            data["default"] = self.default

        if self.trial is not None:
            data["trial"] = CheckoutPlanTrial.__json_encode__(self.trial)

        if self.change_path is not None:
            data["changePath"] = self.change_path

        if self.price is not None:
            data["price"] = Price.__json_encode__(self.price)

        if self.seat_price is not None:
            data["seatPrice"] = Price.__json_encode__(self.seat_price)

        if self.savings is not None:
            data["savings"] = CheckoutPlanSavings.__json_encode__(self.savings)

        if self.disabled is not None:
            data["disabled"] = self.disabled

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CheckoutPlan":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("description") is not None:
            kwargs["description"] = data["description"]

        if data.get("billingInterval") is not None:
            kwargs["billing_interval"] = commonv1.Interval.__json_decode__(
                data["billingInterval"]
            )

        if data.get("group") is not None:
            kwargs["group"] = CheckoutPlanGroup.__json_decode__(data["group"])

        if data.get("revision") is not None:
            kwargs["revision"] = CheckoutPlanRevision.__json_decode__(data["revision"])

        if data.get("current") is not None:
            kwargs["current"] = data["current"]

        if data.get("selected") is not None:
            kwargs["selected"] = data["selected"]

        if data.get("default") is not None:
            kwargs["default"] = data["default"]

        if data.get("trial") is not None:
            kwargs["trial"] = CheckoutPlanTrial.__json_decode__(data["trial"])

        if data.get("changePath") is not None:
            kwargs["change_path"] = data["changePath"]

        if data.get("price") is not None:
            kwargs["price"] = Price.__json_decode__(data["price"])

        if data.get("seatPrice") is not None:
            kwargs["seat_price"] = Price.__json_decode__(data["seatPrice"])

        if data.get("savings") is not None:
            kwargs["savings"] = CheckoutPlanSavings.__json_decode__(data["savings"])

        if data.get("disabled") is not None:
            kwargs["disabled"] = data["disabled"]

        return CheckoutPlan(**kwargs)
