import pytest
from playwright.sync_api import expect

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses",
              wait_until='networkidle')

    courses_header = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_header).to_be_visible()
    expect(courses_header).to_have_text('Courses')

    courses_empty_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_empty_icon).to_be_visible()

    courses_empty_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_empty_text).to_be_visible()
    expect(courses_empty_text).to_have_text('There is no results')

    courses_empty_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_empty_description).to_be_visible()
    expect(courses_empty_description).to_have_text('Results from the load test pipeline will be displayed here')

