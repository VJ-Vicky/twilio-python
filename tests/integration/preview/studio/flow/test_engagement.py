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


class EngagementTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.studio.flows(sid="FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .engagements.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/Studio/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Engagements',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "previous_page_url": null,
                    "next_page_url": null,
                    "url": "https://preview.twilio.com/Studio/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Engagements?PageSize=50&Page=0",
                    "page": 0,
                    "first_page_url": "https://preview.twilio.com/Studio/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Engagements?PageSize=50&Page=0",
                    "page_size": 50,
                    "key": "engagements"
                },
                "engagements": []
            }
            '''
        ))

        actual = self.client.preview.studio.flows(sid="FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                           .engagements.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.studio.flows(sid="FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .engagements(sid="FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/Studio/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Engagements/FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "flow_sid": "FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "contact_sid": "FCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "contact_channel_address": "+14155555555",
                "status": "ended",
                "context": {},
                "date_created": "2017-11-06T12:00:00Z",
                "date_updated": null,
                "url": "https://preview.twilio.com/Studio/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Engagements/FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "steps": "https://preview.twilio.com/Studio/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Engagements/FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Steps"
                }
            }
            '''
        ))

        actual = self.client.preview.studio.flows(sid="FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                           .engagements(sid="FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.studio.flows(sid="FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .engagements.create(to="+15558675310", from_="+15017122661")

        values = {'To': "+15558675310", 'From': "+15017122661", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/Studio/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Engagements',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "url": "https://preview.twilio.com/Studio/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Engagements/FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "flow_sid": "FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "context": {
                    "flow": {
                        "first_name": "Foo"
                    }
                },
                "contact_sid": "FCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "contact_channel_address": "+18001234567",
                "status": "active",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "links": {
                    "steps": "https://preview.twilio.com/Studio/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Engagements/FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Steps"
                }
            }
            '''
        ))

        actual = self.client.preview.studio.flows(sid="FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                           .engagements.create(to="+15558675310", from_="+15017122661")

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.studio.flows(sid="FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .engagements(sid="FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://preview.twilio.com/Studio/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Engagements/FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.preview.studio.flows(sid="FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                           .engagements(sid="FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.assertTrue(actual)
