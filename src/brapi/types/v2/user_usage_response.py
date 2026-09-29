# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UserUsageResponse", "Usage", "UsageSubscriptionPeriod", "UsageUsageWindow"]


class UsageSubscriptionPeriod(BaseModel):
    end: Optional[datetime] = None

    start: Optional[datetime] = None


class UsageUsageWindow(BaseModel):
    end: datetime

    start: datetime

    type: Literal["billing-cycle", "rolling-30d"]


class Usage(BaseModel):
    current_usage: int = FieldInfo(alias="currentUsage")

    plan_limit: int = FieldInfo(alias="planLimit")

    plan_name: Literal["free", "startup", "pro"] = FieldInfo(alias="planName")

    remaining_usage: int = FieldInfo(alias="remainingUsage")

    subscription_period: UsageSubscriptionPeriod = FieldInfo(alias="subscriptionPeriod")

    usage_window: UsageUsageWindow = FieldInfo(alias="usageWindow")


class UserUsageResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""

    usage: Usage
