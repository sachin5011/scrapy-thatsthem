import scrapy
from ..items import ThatsthemItem


class ThatsThemSpider(scrapy.Spider):
    name = "thatsthem"
    origin_email = "https://thatsthem.com/email/"
    email_list = ["deborahgates57@gmail.com", "jhon-713@hotmail.com", "s-15power@hotmail.com", "t--mcq@yahoo.com",
                  "m-4e2@live.com"]
    # "https://thatsthem.com/email/test.3dmick@gmail.com"
    start_urls = [
        # origin_email+email_list[4]
        "https://thatsthem.com/email/" + x for x in email_list
    ]

    def parse(self, response):
        items = ThatsthemItem()

        number = response.css(".web::text").extract()
        email = list(set([x for x in number if "@" in x]))
        found_number = list(set([x.strip("\r\n") if "-" in x and "@" not in x else "NA" for x in number]))

        items["email"] = email
        items["number"] = found_number

        yield items
