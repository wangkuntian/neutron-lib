# Copyright 2023 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from neutron_lib._i18n import _
from neutron_lib import exceptions


class UnableToAddExtraGateways(exceptions.NeutronException):
    message = _("Unable to add extra gateways to a router %(router_id)s")


class UnableToRemoveGateways(exceptions.NeutronException):
    message = _("Unable to remove extra gateways from a router %(router_id)s")


class UnableToMatchGateways(exceptions.NeutronException):
    message = _("Unable to match a requested gateway port to"
                " existing gateway ports for router %(router_id)s")


class UnableToAddExtraGatewayPort(exceptions.NeutronException):
    message = _("Unable to add an gateway port to a router %(router_id)s")
