# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class LogAnalyticsQueryPackQueryPaged(Paged):
    """
    A paging container for iterating over a list of :class:`LogAnalyticsQueryPackQuery <azure.mgmt.applicationinsights.v2019_09_01_preview.models.LogAnalyticsQueryPackQuery>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[LogAnalyticsQueryPackQuery]'}
    }

    def __init__(self, *args, **kwargs):

        super(LogAnalyticsQueryPackQueryPaged, self).__init__(*args, **kwargs)
class LogAnalyticsQueryPackPaged(Paged):
    """
    A paging container for iterating over a list of :class:`LogAnalyticsQueryPack <azure.mgmt.applicationinsights.v2019_09_01_preview.models.LogAnalyticsQueryPack>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[LogAnalyticsQueryPack]'}
    }

    def __init__(self, *args, **kwargs):

        super(LogAnalyticsQueryPackPaged, self).__init__(*args, **kwargs)
