# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class TaskChannelTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .task_channels(sid="TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels/TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2014-05-14T10:50:02Z",
                "date_updated": "2014-05-14T23:26:06Z",
                "friendly_name": "Default",
                "sid": "TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "default",
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels/TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .task_channels(sid="TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .task_channels.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "channels": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2014-05-14T10:50:02Z",
                        "date_updated": "2014-05-14T23:26:06Z",
                        "friendly_name": "Default",
                        "sid": "TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "unique_name": "default",
                        "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels/TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels?PageSize=50&Page=0",
                    "key": "channels",
                    "last_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels?PageSize=50&Page=0",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 1,
                    "previous_page_url": null,
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .task_channels.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "channels": [],
                "meta": {
                    "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels?PageSize=50&Page=0",
                    "key": "channels",
                    "last_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels?PageSize=50&Page=0",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .task_channels.list()

        self.assertIsNotNone(actual)
