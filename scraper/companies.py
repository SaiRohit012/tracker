# companies.py — Master company list with ATS type and career page URLs
# ATS types: "greenhouse", "lever", "workday", "playwright", "linkedin_rss"
#
# Last audited: July 2026
#
# Changes vs previous version:
#   FIXED  — Google India: ats was "workday" but URL is careers.google.com (Google's own
#             custom site, not myworkdayjobs.com) -> corrected to "playwright"
#   FIXED  — Nvidia India: ats was "playwright" but URL is nvidia.wd5.myworkdayjobs.com
#             (genuine Workday tenant) -> corrected to "workday"
#   FIXED  — Akamai India: ats was "playwright" but URL is akamai.wd1.myworkdayjobs.com
#             (genuine Workday tenant) -> corrected to "workday"
#   FIXED  — Cisco India: ats was "workday" but URL is jobs.cisco.com (Cisco's own
#             custom site, not myworkdayjobs.com) -> corrected to "playwright"
#   FIXED  — Juniper Networks India: ats was "workday" but URL is careers.juniper.net
#             (custom site) -> corrected to "playwright"
#   FIXED  — Palo Alto Networks India: ats was "workday" but URL is
#             jobs.paloaltonetworks.com (custom site) -> corrected to "playwright"
#   FIXED  — Accenture: ats was "workday" but URL is accenture.com/in-en/careers
#             (custom site) -> corrected to "playwright"
#   FIXED  — Twilio India: ats was "workday" and URL was a Greenhouse public board page
#             (boards.greenhouse.io/twilio, not an API endpoint) -> corrected ats to
#             "greenhouse" and URL to the actual Greenhouse API endpoint
#
#   NOTE ON REVISION 1's ADDITIONS — these came from a raw BITS placement-portal
#   "station name" list, not from live verification of each career page. For every
#   genuinely new company, the "ats" field defaults to "playwright" (generic scrape)
#   rather than guessing an exact Workday tenant subdomain or Greenhouse/Lever board
#   slug — getting that slug wrong silently breaks an API-based scraper, whereas
#   playwright degrades gracefully. Where a company is widely known to run on
#   Workday/Greenhouse, that's flagged in a NOTE so it can be upgraded once confirmed
#   live. A handful of small/unlisted firms had no confidently identifiable public
#   career-page domain — flagged explicitly rather than fabricated.
#
#   REVISION 2 (July 19, 2026) — added the user's "God Tier" through "B-" quant-fund
#   and big-tech tier list (~90 companies). Verified live via web search where possible:
#     CONFIRMED  — DRW is genuinely Greenhouse-backed (job-boards.greenhouse.io/drweng)
#     CONFIRMED  — Renaissance Technologies, Citadel, Point72, Hudson River Trading,
#                  Optiver, Two Sigma, Akuna Capital, DE Shaw all run fully custom
#                  career sites (not on a public ATS API) -> ats set to "playwright"
#                  with the real, verified URL.
#   Everything else in this revision defaults to "playwright" with a NOTE flag, same
#   policy as Revision 1: many quant funds (Jump Trading, Millennium, AQR, SIG,
#   G-Research, WorldQuant, Squarepoint, Virtu, Maven Securities, Five Rings, Voleon,
#   XTX Markets, Quadrature, Radix, TGS, Arrowstreet, PDT) almost certainly have a
#   working public careers page at the domain guessed below, but the exact URL path
#   and whether it's secretly Greenhouse/Lever-backed was NOT individually verified —
#   confirm before switching any of these to an API-based ats type.
#   "Ridgewater Capital" could not be confidently identified as a real, distinct firm
#   (not a recognized name in the quant-fund space) — flagged with an empty URL rather
#   than a guessed one; please double-check the intended firm name.
#
#   SKIPPED AS DUPLICATES (already exist above under an existing entry, so NOT
#   re-added): Jane Street, D.E. Shaw, Tower Research Capital, Google, Amazon/AWS,
#   Microsoft, Meta, Apple, Nvidia, LinkedIn, Airbnb, Databricks, Stripe, PayPal,
#   Coinbase, Bloomberg, Snowflake, Rubrik, Notion, Coupang, Adobe, Cloudflare, Oracle,
#   Atlassian, Salesforce, Uber, JPMorgan Chase, Morgan Stanley, Booking.com,
#   BlackRock, IBM, Citi, Goldman Sachs, Walmart.

COMPANIES = [
    # ── Big Tech ──────────────────────────────────────────────────────────────
    # FIXED: was "workday" — careers.google.com is Google's own site, not Workday
    {"name": "Google India",             "ats": "playwright", "url": "https://careers.google.com/jobs/results/?location=India&q="},
    {"name": "Amazon / AWS",             "ats": "playwright", "url": "https://www.amazon.jobs/en/search?base_query={role}&loc_query=India"},
    {"name": "Microsoft India",          "ats": "playwright", "url": "https://jobs.microsoft.com/en/us/search?q={role}&lc=India"},
    {"name": "Meta India",               "ats": "playwright", "url": "https://www.metacareers.com/jobs?offices[0]=India&q={role}"},
    {"name": "Apple India",              "ats": "playwright", "url": "https://jobs.apple.com/en-us/search?location=india-IND&search={role}"},
    {"name": "Adobe India",              "ats": "workday",    "url": "https://adobe.wd5.myworkdayjobs.com/external_experienced/jobs?q={role}&locations=India"},
    # FIXED: was "playwright" — this is a genuine Workday tenant URL
    {"name": "Nvidia India",             "ats": "workday",    "url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/jobs?q={role}&locations=India"},
    {"name": "Qualcomm India",           "ats": "workday",    "url": "https://qualcomm.wd5.myworkdayjobs.com/External/jobs?q={role}&locations=India"},
    {"name": "LinkedIn India",           "ats": "playwright", "url": "https://careers.linkedin.com/jobs?keywords={role}&location=India"},
    {"name": "Walmart Global Tech",      "ats": "workday",    "url": "https://walmart.wd5.myworkdayjobs.com/WalmartExternal/jobs?q={role}&locations=India"},
    {"name": "MediaTek India",           "ats": "playwright", "url": "https://careers.mediatek.com/eREC/JobSearch/Index?JobKeywords={role}&CountryID=IN"},
    {"name": "Micron Technology",        "ats": "workday",    "url": "https://micron.wd1.myworkdayjobs.com/External/jobs?q={role}&locations=India"},
    {"name": "ByteDance India",          "ats": "playwright", "url": "https://jobs.bytedance.com/en/position?keywords={role}&location=India"},
    # FIXED: was "playwright" — this is a genuine Workday tenant URL
    {"name": "Akamai India",             "ats": "workday",    "url": "https://akamai.wd1.myworkdayjobs.com/en-US/External/jobs?q={role}&locations=India"},
    {"name": "Airbnb India",             "ats": "greenhouse", "greenhouse_id": "airbnb",       "url": "https://api.greenhouse.io/v1/boards/airbnb/jobs"},
    {"name": "Coupang India",            "ats": "greenhouse", "greenhouse_id": "coupang",      "url": "https://api.greenhouse.io/v1/boards/coupang/jobs"},
    {"name": "Zalando India",            "ats": "playwright", "url": "https://jobs.zalando.com/en/jobs?locations=India&search={role}"},
    {"name": "LG Ad Solutions India",    "ats": "playwright", "url": "https://lgads.tv/careers/"},
    {"name": "Wayfair India",            "ats": "greenhouse", "greenhouse_id": "wayfair",      "url": "https://api.greenhouse.io/v1/boards/wayfair/jobs"},
    # NEW: AMD India — Bengaluru/Hyderabad
    # NOTE: widely believed to run on Workday; verify exact tenant before switching ats type
    {"name": "AMD India",                "ats": "playwright", "url": "https://careers.amd.com/careers-home/jobs?location=India&keywords={role}"},
    # NEW: ARM Embedded Technologies — Bengaluru
    {"name": "ARM Embedded Technologies","ats": "playwright", "url": "https://careers.arm.com/en/search-results?keywords={role}&location=India"},
    # NEW: Marvell Technology
    # NOTE: widely believed to run on Workday; verify exact tenant before switching ats type
    {"name": "Marvell Technology",       "ats": "playwright", "url": "https://careers.marvell.com/search-results?keywords={role}&location=India"},
    # NEW: NXP India — Noida
    # NOTE: widely believed to run on Workday; verify exact tenant before switching ats type
    {"name": "NXP India",                "ats": "playwright", "url": "https://www.nxp.com/careers-home/jobs?location=India&keywords={role}"},
    # NEW: Onsemi (On Semiconductor)
    # NOTE: widely believed to run on Workday; verify exact tenant before switching ats type
    {"name": "Onsemi",                   "ats": "playwright", "url": "https://www.onsemi.com/careers/job-search?keywords={role}&location=India"},
    # NEW: Skyworks Solutions — Bengaluru
    {"name": "Skyworks Solutions",       "ats": "playwright", "url": "https://www.skyworksinc.com/en/Careers"},
    # NEW: Western Digital (SanDisk) — Bengaluru
    # NOTE: widely believed to run on Workday; verify exact tenant before switching ats type
    {"name": "Western Digital",          "ats": "playwright", "url": "https://jobs.westerndigital.com/search-jobs?k={role}&l=India"},
    # NEW: Microchip Technology / Microsemi
    {"name": "Microchip Technology",     "ats": "playwright", "url": "https://careers.microchip.com/en/search-results?keywords={role}&location=India"},
    # NEW: Infineon Technologies India — Supply Chain and other roles
    {"name": "Infineon Technologies India","ats": "playwright","url": "https://www.infineon.com/cms/en/careers/search-and-apply/?query={role}&location=India"},
    # NEW: Astera Labs
    # NOTE: possibly Greenhouse-backed; verify board slug before switching ats type
    {"name": "Astera Labs",              "ats": "playwright", "url": "https://www.asteralabs.com/careers/"},

    # ── Finance / Quant ───────────────────────────────────────────────────────
    {"name": "Goldman Sachs India",      "ats": "playwright", "url": "https://higher.gs.com/roles?query={role}&region=India"},
    {"name": "JP Morgan India",          "ats": "playwright", "url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/jobs?keyword={role}&location=India&locationId=300000000289360&locationLevel=country"},
    {"name": "Morgan Stanley India",     "ats": "playwright", "url": "https://morganstanley.eightfold.ai/careers?location=india&query={role}"},
    {"name": "D.E. Shaw India",          "ats": "playwright", "url": "https://www.deshawindia.com/careers/opportunities?department=All&location=India"},
    {"name": "Jane Street India",        "ats": "playwright", "url": "https://www.janestreet.com/join-jane-street/open-roles/?type=experienced-hire&location=india"},
    {"name": "Tower Research Capital",   "ats": "playwright", "url": "https://www.tower-research.com/open-positions"},
    {"name": "Arcesium",                 "ats": "greenhouse", "greenhouse_id": "arcesium",     "url": "https://api.greenhouse.io/v1/boards/arcesium/jobs"},
    {"name": "Bloomberg India",          "ats": "playwright", "url": "https://careers.bloomberg.com/job/search?el=India&q={role}"},
    {"name": "BlackRock India",          "ats": "workday",    "url": "https://blackrock.wd1.myworkdayjobs.com/en-US/BlackRock_Experienced_Professionals/jobs?q={role}&locations=India"},
    {"name": "Visa India",               "ats": "workday",    "url": "https://visa.wd5.myworkdayjobs.com/en-US/Visa/jobs?q={role}&locationCountry=bc33aa3152ec42d4995f4791a3b30e02"},
    {"name": "HSBC Tech India",          "ats": "playwright", "url": "https://mycareer.hsbc.com/en_GB/external/SearchJobs/{role}?projectOffset=0&locations=India"},
    {"name": "Zeta",                     "ats": "greenhouse", "greenhouse_id": "zeta",         "url": "https://api.greenhouse.io/v1/boards/zeta/jobs"},
    {"name": "Societe Generale India",   "ats": "playwright", "url": "https://careers.societegenerale.com/en/job-offers?q={role}&location=India"},
    {"name": "Barclays India",           "ats": "playwright", "url": "https://search.jobs.barclays/search-jobs/{role}/India/22545/1/2/3/3/0/0"},
    {"name": "Citi India",               "ats": "workday",    "url": "https://citi.wd5.myworkdayjobs.com/en-US/ICG/jobs?q={role}&locations=India"},
    {"name": "Kotak Mahindra Bank",      "ats": "playwright", "url": "https://kotakbank.com/personal/about-us/careers/current-openings.html"},
    {"name": "Kotak Securities",         "ats": "playwright", "url": "https://kotaksecurities.com/careers/"},
    {"name": "Coinbase India",           "ats": "greenhouse", "greenhouse_id": "coinbase",     "url": "https://api.greenhouse.io/v1/boards/coinbase/jobs"},
    {"name": "Deutsche Bank India",      "ats": "workday",    "url": "https://db.wd3.myworkdayjobs.com/en-US/DBWebsite/jobs?q={role}&locations=India"},
    {"name": "American Express India",   "ats": "playwright", "url": "https://jobs.americanexpress.com/india/jobs?q={role}"},
    {"name": "Fidelity Investments India","ats": "playwright", "url": "https://jobs.fidelity.com/in/jobs?q={role}"},
    {"name": "Mastercard India",         "ats": "playwright", "url": "https://careers.mastercard.com/us/en/search-results?keywords={role}&location=India"},
    {"name": "Equifax India",            "ats": "playwright", "url": "https://careers.equifax.com/en/jobs/?keyword={role}&location=India"},
    # NEW: Moody's Analytics
    # NOTE: widely believed to run on Workday; verify exact tenant before switching ats type
    {"name": "Moody's Analytics",        "ats": "playwright", "url": "https://careers.moodys.com/careers-home/jobs?location=India&keywords={role}"},
    # NEW: Morningstar — Index Management and Analytics
    # NOTE: widely believed to run on Workday; verify exact tenant before switching ats type
    {"name": "Morningstar India",        "ats": "playwright", "url": "https://careers.morningstar.com/search-jobs?k={role}&l=India"},
    # NEW: MSCI Services
    {"name": "MSCI Services",            "ats": "playwright", "url": "https://www.msci.com/who-we-are/careers"},
    # NEW: Synchrony — API/Backend/Front End/Full Stack roles all map here
    # NOTE: widely believed to run on Workday; verify exact tenant before switching ats type
    {"name": "Synchrony",                "ats": "playwright", "url": "https://synchronycareers.com/search-jobs?k={role}&l=India"},
    # NEW: Swiss Re Global Business Solutions India
    # NOTE: widely believed to run on Workday; verify exact tenant before switching ats type
    {"name": "Swiss Re GBS India",       "ats": "playwright", "url": "https://careers.swissre.com/search-jobs?k={role}&l=India"},

    # ── Fintech / Payments ────────────────────────────────────────────────────
    {"name": "Stripe India",             "ats": "playwright", "url": "https://stripe.com/jobs/search?location=India&query={role}"},
    {"name": "PayPal India",             "ats": "workday",    "url": "https://paypal.wd1.myworkdayjobs.com/jobs?q={role}&locations=India"},
    {"name": "Razorpay",                 "ats": "lever",      "lever_id": "razorpay",          "url": "https://api.lever.co/v0/postings/razorpay?mode=json"},
    {"name": "Intuit India",             "ats": "workday",    "url": "https://intuit.wd1.myworkdayjobs.com/en-US/Intuit_Careers/jobs?q={role}&locations=India"},
    {"name": "Rippling India",           "ats": "greenhouse", "greenhouse_id": "rippling",     "url": "https://api.greenhouse.io/v1/boards/rippling/jobs"},
    {"name": "PhonePe",                  "ats": "lever",      "lever_id": "phonepe",           "url": "https://api.lever.co/v0/postings/phonepe?mode=json"},
    {"name": "Zerodha",                  "ats": "playwright", "url": "https://zerodha.com/careers/#openings"},
    {"name": "Groww",                    "ats": "greenhouse", "greenhouse_id": "groww",        "url": "https://api.greenhouse.io/v1/boards/groww/jobs"},
    {"name": "CoinSwitch",               "ats": "lever",      "lever_id": "coinswitch",        "url": "https://api.lever.co/v0/postings/coinswitch?mode=json"},
    {"name": "Yubi",                     "ats": "lever",      "lever_id": "yubi",              "url": "https://api.lever.co/v0/postings/yubi?mode=json"},
    {"name": "Slice",                    "ats": "lever",      "lever_id": "sliceit",           "url": "https://api.lever.co/v0/postings/sliceit?mode=json"},
    {"name": "smallcase",                "ats": "greenhouse", "greenhouse_id": "smallcase",    "url": "https://api.greenhouse.io/v1/boards/smallcase/jobs"},
    {"name": "Jeeves",                   "ats": "greenhouse", "greenhouse_id": "jeeveshq",     "url": "https://api.greenhouse.io/v1/boards/jeeveshq/jobs"},
    {"name": "Khatabook",                "ats": "greenhouse", "greenhouse_id": "khatabook",    "url": "https://api.greenhouse.io/v1/boards/khatabook/jobs"},
    {"name": "Progcap",                  "ats": "greenhouse", "greenhouse_id": "progcap",      "url": "https://api.greenhouse.io/v1/boards/progcap/jobs"},
    {"name": "mPokket",                  "ats": "playwright", "url": "https://mpokket.com/careers"},
    {"name": "Simpl",                    "ats": "greenhouse", "greenhouse_id": "simpl",        "url": "https://api.greenhouse.io/v1/boards/simpl/jobs"},
    {"name": "Finicity",                 "ats": "workday",    "url": "https://mastercard.wd1.myworkdayjobs.com/en-US/External/jobs?q={role}&locations=India"},
    {"name": "Paytm",                    "ats": "lever",      "lever_id": "paytm",             "url": "https://api.lever.co/v0/postings/paytm?mode=json"},
    {"name": "Blackhawk Network India",  "ats": "lever",      "lever_id": "blackhawknetwork",  "url": "https://api.lever.co/v0/postings/blackhawknetwork?mode=json"},
    {"name": "super.money",              "ats": "playwright", "url": "https://super.money/careers"},
    # NEW: Navi Technologies — Business Analyst / SDE roles
    {"name": "Navi Technologies",        "ats": "playwright", "url": "https://navi.com/careers/"},
    # NEW: Prosperr.io
    # NOTE: startup, domain unverified — confirm before deploying
    {"name": "Prosperr.io",              "ats": "playwright", "url": "https://prosperr.io/careers"},
    # NEW: Scapia Technology
    # NOTE: domain unverified — confirm before deploying
    {"name": "Scapia Technology",        "ats": "playwright", "url": "https://www.scapia.club/careers"},
    # NEW: Stampmyvisa — AI&ML / Product / Software roles all map here
    # NOTE: domain unverified — confirm before deploying
    {"name": "Stampmyvisa",              "ats": "playwright", "url": "https://stampmyvisa.com/careers"},
    # NEW: Svamaan Financial Services
    # NOTE: domain unverified — confirm before deploying
    {"name": "Svamaan Financial Services","ats": "playwright", "url": "https://svamaan.com/careers"},

    # ── Infra / Cloud / Security ──────────────────────────────────────────────
    {"name": "Rubrik India",             "ats": "greenhouse", "greenhouse_id": "rubrik",       "url": "https://api.greenhouse.io/v1/boards/rubrik/jobs"},
    # FIXED: was "workday" — jobs.cisco.com is Cisco's own site, not myworkdayjobs.com
    {"name": "Cisco India",              "ats": "playwright", "url": "https://jobs.cisco.com/jobs/SearchJobs/{role}?listFilterMode=1&location=India"},
    {"name": "IBM India",                "ats": "playwright", "url": "https://www.ibm.com/employment/in/en/search/?q={role}&options=Location%3AIndia"},
    {"name": "Oracle India",             "ats": "playwright", "url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/jobs?keyword={role}&location=India"},
    # FIXED: was "workday" — careers.juniper.net is Juniper's own site, not myworkdayjobs.com
    {"name": "Juniper Networks India",   "ats": "playwright", "url": "https://careers.juniper.net/careers/jobs?q={role}&location=India"},
    {"name": "Netskope India",           "ats": "greenhouse", "greenhouse_id": "netskope",     "url": "https://api.greenhouse.io/v1/boards/netskope/jobs"},
    {"name": "Confluent India",          "ats": "greenhouse", "greenhouse_id": "confluent",    "url": "https://api.greenhouse.io/v1/boards/confluent/jobs"},
    {"name": "ServiceNow India",         "ats": "playwright", "url": "https://jobs.smartrecruiters.com/ServiceNow/search?keyword={role}&location=India"},
    {"name": "Databricks India",         "ats": "greenhouse", "greenhouse_id": "databricks",   "url": "https://api.greenhouse.io/v1/boards/databricks/jobs"},
    {"name": "Snowflake India",          "ats": "greenhouse", "greenhouse_id": "snowflake",    "url": "https://api.greenhouse.io/v1/boards/snowflake/jobs"},
    {"name": "GitLab India",             "ats": "greenhouse", "greenhouse_id": "gitlab",       "url": "https://api.greenhouse.io/v1/boards/gitlab/jobs"},
    # FIXED: was "workday" — jobs.paloaltonetworks.com is PANW's own site, not myworkdayjobs.com
    {"name": "Palo Alto Networks India", "ats": "playwright", "url": "https://jobs.paloaltonetworks.com/en/jobs?q={role}&location=India"},
    {"name": "Uptycs",                   "ats": "greenhouse", "greenhouse_id": "uptycs",       "url": "https://api.greenhouse.io/v1/boards/uptycs/jobs"},
    {"name": "Fortanix",                 "ats": "greenhouse", "greenhouse_id": "fortanix",     "url": "https://api.greenhouse.io/v1/boards/fortanix/jobs"},
    {"name": "Safe Security",            "ats": "greenhouse", "greenhouse_id": "safesecurity", "url": "https://api.greenhouse.io/v1/boards/safesecurity/jobs"},
    {"name": "Teradata India",           "ats": "workday",    "url": "https://teradata.wd1.myworkdayjobs.com/Teradata_Careers/jobs?q={role}&locations=India"},
    {"name": "Hyland India",             "ats": "playwright", "url": "https://www.hyland.com/en/company/careers/job-search?q={role}&location=India"},
    {"name": "Siemens India",            "ats": "playwright", "url": "https://jobs.siemens.com/careers?query={role}&location=India"},
    {"name": "Experian India",           "ats": "workday",    "url": "https://experian.wd3.myworkdayjobs.com/Experian_Careers/jobs?q={role}&locations=India"},
    {"name": "DocuSign India",           "ats": "greenhouse", "greenhouse_id": "docusign",     "url": "https://api.greenhouse.io/v1/boards/docusign/jobs"},
    {"name": "Elastic India",            "ats": "greenhouse", "greenhouse_id": "elastic",      "url": "https://api.greenhouse.io/v1/boards/elastic/jobs"},
    {"name": "MongoDB India",            "ats": "greenhouse", "greenhouse_id": "mongodb",      "url": "https://api.greenhouse.io/v1/boards/mongodb/jobs"},
    {"name": "Cloudflare India",         "ats": "greenhouse", "greenhouse_id": "cloudflare",   "url": "https://api.greenhouse.io/v1/boards/cloudflare/jobs"},
    # FIXED: was ats="workday" with a Greenhouse public-board URL (not even an API
    # endpoint) — corrected to ats="greenhouse" with the real API endpoint
    {"name": "Twilio India",             "ats": "greenhouse", "greenhouse_id": "twilio",       "url": "https://api.greenhouse.io/v1/boards/twilio/jobs"},
    {"name": "Samsara India",            "ats": "greenhouse", "greenhouse_id": "samsara",      "url": "https://api.greenhouse.io/v1/boards/samsara/jobs"},
    # NEW: Redwood Software
    # NOTE: possibly Greenhouse-backed; verify board slug before switching ats type
    {"name": "Redwood Software",         "ats": "playwright", "url": "https://redwood.com/careers/"},
    # NEW: Orange Business India — Cloud Infrastructure & Migration
    {"name": "Orange Business India",    "ats": "playwright", "url": "https://careers.orange-business.com/"},

    # ── Unicorns / Startups ───────────────────────────────────────────────────
    {"name": "Flipkart",                 "ats": "playwright", "url": "https://www.flipkartcareers.com/#!/joblist"},
    {"name": "Swiggy",                   "ats": "lever",      "lever_id": "swiggy",            "url": "https://api.lever.co/v0/postings/swiggy?mode=json"},
    {"name": "Zomato",                   "ats": "playwright", "url": "https://www.zomato.com/careers#jobs"},
    {"name": "Freshworks",               "ats": "greenhouse", "greenhouse_id": "freshworks",   "url": "https://api.greenhouse.io/v1/boards/freshworks/jobs"},
    {"name": "Zoho",                     "ats": "playwright", "url": "https://careers.zohocorp.com/jobs/Careers"},
    {"name": "Atlassian India",          "ats": "greenhouse", "greenhouse_id": "atlassian",    "url": "https://api.greenhouse.io/v1/boards/atlassian/jobs"},
    {"name": "Meesho",                   "ats": "lever",      "lever_id": "meesho",            "url": "https://api.lever.co/v0/postings/meesho?mode=json"},
    {"name": "CRED",                     "ats": "lever",      "lever_id": "dreamplug",         "url": "https://api.lever.co/v0/postings/dreamplug?mode=json"},
    {"name": "Zepto",                    "ats": "lever",      "lever_id": "zepto",             "url": "https://api.lever.co/v0/postings/zepto?mode=json"},
    {"name": "Dream11",                  "ats": "playwright", "url": "https://careers.dream11.com/"},
    {"name": "Ola / Ola Electric",       "ats": "playwright", "url": "https://careers.ola.com/jobs?q={role}"},
    {"name": "PolicyBazaar",             "ats": "playwright", "url": "https://jobs.policybazaar.com/"},
    {"name": "Uber India",               "ats": "playwright", "url": "https://www.uber.com/us/en/careers/jobs/?query={role}&location=India"},
    {"name": "Booking.com India",        "ats": "playwright", "url": "https://jobs.booking.com/careers?q={role}&location=India"},
    {"name": "Agoda India",              "ats": "playwright", "url": "https://careersatagoda.com/jobs/?s={role}&location=India"},
    {"name": "Curefit",                  "ats": "greenhouse", "greenhouse_id": "curefit",      "url": "https://api.greenhouse.io/v1/boards/curefit/jobs"},
    {"name": "Notion India",             "ats": "greenhouse", "greenhouse_id": "notion",       "url": "https://api.greenhouse.io/v1/boards/notion/jobs"},
    {"name": "Warner Bros Discovery",    "ats": "workday",    "url": "https://warnerbros.wd5.myworkdayjobs.com/global/jobs?q={role}&locations=India"},
    {"name": "MakeMyTrip",               "ats": "playwright", "url": "https://careers.makemytrip.com/prod/jobs"},
    {"name": "InMobi",                   "ats": "greenhouse", "greenhouse_id": "inmobi",       "url": "https://api.greenhouse.io/v1/boards/inmobi/jobs"},
    {"name": "Nykaa Tech",               "ats": "playwright", "url": "https://careers.nykaa.com/jobs?q={role}"},
    {"name": "Cars24",                   "ats": "playwright", "url": "https://www.cars24.com/careers/"},
    {"name": "Myntra",                   "ats": "playwright", "url": "https://careers.myntra.com/jobs?q={role}"},
    {"name": "ShareChat",                "ats": "greenhouse", "greenhouse_id": "sharechat",    "url": "https://api.greenhouse.io/v1/boards/sharechat/jobs"},
    {"name": "Urban Company",            "ats": "greenhouse", "greenhouse_id": "urbancompany", "url": "https://api.greenhouse.io/v1/boards/urbancompany/jobs"},
    {"name": "Cleartrip",                "ats": "playwright", "url": "https://careers.cleartrip.com/"},
    {"name": "Delhivery",                "ats": "playwright", "url": "https://careers.delhivery.com/jobs?q={role}"},
    {"name": "Lenskart",                 "ats": "playwright", "url": "https://careers.lenskart.com/jobs?q={role}"},
    # NEW: Netradyne — Bengaluru
    # NOTE: possibly Greenhouse-backed; verify board slug before switching ats type
    {"name": "Netradyne",                "ats": "playwright", "url": "https://www.netradyne.com/careers"},
    # NEW: OfBusiness
    {"name": "OfBusiness",               "ats": "playwright", "url": "https://www.ofbusiness.com/careers"},
    # NEW: Spinny
    {"name": "Spinny",                   "ats": "playwright", "url": "https://www.spinny.com/careers/"},
    # NEW: Virgio — UI Engineering
    # NOTE: domain unverified — confirm before deploying
    {"name": "Virgio",                   "ats": "playwright", "url": "https://virgio.com/careers"},
    # NEW: Zetwerk — Business Systems / Procurement / Solar / Structural Steel roles all map here
    {"name": "Zetwerk",                  "ats": "playwright", "url": "https://www.zetwerk.com/careers/"},
    # NEW: Dashverse
    # NOTE: startup, domain unverified — confirm before deploying
    {"name": "Dashverse",                "ats": "playwright", "url": "https://www.dashverse.com/careers"},
    # NEW: Teleparty — Android / Data Engineering / Full Stack / iOS roles all map here
    # NOTE: domain unverified — confirm before deploying
    {"name": "Teleparty",                "ats": "playwright", "url": "https://www.teleparty.com/careers"},

    # ── SaaS / Growth ─────────────────────────────────────────────────────────
    {"name": "Juspay",                   "ats": "greenhouse", "greenhouse_id": "juspay",       "url": "https://api.greenhouse.io/v1/boards/juspay/jobs"},
    {"name": "Atlan",                    "ats": "greenhouse", "greenhouse_id": "atlan",        "url": "https://api.greenhouse.io/v1/boards/atlan/jobs"},
    {"name": "Instabase",                "ats": "greenhouse", "greenhouse_id": "instabase",    "url": "https://api.greenhouse.io/v1/boards/instabase/jobs"},
    {"name": "Yellow.ai",                "ats": "lever",      "lever_id": "yellowmessenger",   "url": "https://api.lever.co/v0/postings/yellowmessenger?mode=json"},
    {"name": "Hevo Data",                "ats": "lever",      "lever_id": "hevo",              "url": "https://api.lever.co/v0/postings/hevo?mode=json"},
    {"name": "Observe.AI",               "ats": "greenhouse", "greenhouse_id": "observeai",    "url": "https://api.greenhouse.io/v1/boards/observeai/jobs"},
    {"name": "Harness",                  "ats": "greenhouse", "greenhouse_id": "harness",      "url": "https://api.greenhouse.io/v1/boards/harness/jobs"},
    {"name": "Plivo",                    "ats": "greenhouse", "greenhouse_id": "plivo",        "url": "https://api.greenhouse.io/v1/boards/plivo/jobs"},
    {"name": "LambdaTest",               "ats": "lever",      "lever_id": "lambdatest",        "url": "https://api.lever.co/v0/postings/lambdatest?mode=json"},
    {"name": "Multiplier",               "ats": "greenhouse", "greenhouse_id": "multiplier",   "url": "https://api.greenhouse.io/v1/boards/multiplier/jobs"},
    {"name": "Simpplr",                  "ats": "greenhouse", "greenhouse_id": "simpplr",      "url": "https://api.greenhouse.io/v1/boards/simpplr/jobs"},
    {"name": "Pixis",                    "ats": "greenhouse", "greenhouse_id": "pixis",        "url": "https://api.greenhouse.io/v1/boards/pixis/jobs"},
    {"name": "Moveworks",                "ats": "greenhouse", "greenhouse_id": "moveworks",    "url": "https://api.greenhouse.io/v1/boards/moveworks/jobs"},
    {"name": "Sigmoid",                  "ats": "greenhouse", "greenhouse_id": "sigmoid",      "url": "https://api.greenhouse.io/v1/boards/sigmoid/jobs"},
    {"name": "Tenstorrent",              "ats": "greenhouse", "greenhouse_id": "tenstorrent",  "url": "https://api.greenhouse.io/v1/boards/tenstorrent/jobs"},
    {"name": "DataWeave",                "ats": "greenhouse", "greenhouse_id": "dataweave",    "url": "https://api.greenhouse.io/v1/boards/dataweave/jobs"},
    {"name": "Contentstack",             "ats": "greenhouse", "greenhouse_id": "contentstack", "url": "https://api.greenhouse.io/v1/boards/contentstack/jobs"},
    {"name": "Builder.ai",               "ats": "greenhouse", "greenhouse_id": "builderai",    "url": "https://api.greenhouse.io/v1/boards/builderai/jobs"},
    {"name": "SaaS Labs",                "ats": "greenhouse", "greenhouse_id": "saaslabs",     "url": "https://api.greenhouse.io/v1/boards/saaslabs/jobs"},
    {"name": "Seclore",                  "ats": "playwright", "url": "https://www.seclore.com/careers/"},
    {"name": "Catchpoint",               "ats": "greenhouse", "greenhouse_id": "catchpoint",   "url": "https://api.greenhouse.io/v1/boards/catchpoint/jobs"},
    {"name": "HackerEarth",              "ats": "playwright", "url": "https://www.hackerearth.com/company/hackerearth/jobs/"},
    {"name": "Postman",                  "ats": "greenhouse", "greenhouse_id": "postman",      "url": "https://api.greenhouse.io/v1/boards/postman/jobs"},
    {"name": "BrowserStack",             "ats": "greenhouse", "greenhouse_id": "browserstack", "url": "https://api.greenhouse.io/v1/boards/browserstack/jobs"},
    {"name": "Chargebee",                "ats": "greenhouse", "greenhouse_id": "chargebee",    "url": "https://api.greenhouse.io/v1/boards/chargebee/jobs"},
    {"name": "Darwinbox",                "ats": "greenhouse", "greenhouse_id": "darwinbox",    "url": "https://api.greenhouse.io/v1/boards/darwinbox/jobs"},
    {"name": "Whatfix",                  "ats": "greenhouse", "greenhouse_id": "whatfix",      "url": "https://api.greenhouse.io/v1/boards/whatfix/jobs"},
    {"name": "Salesforce India",         "ats": "workday",    "url": "https://salesforce.wd12.myworkdayjobs.com/en-US/External_Career_Site/jobs?q={role}&locations=India"},
    {"name": "Alphonso",                 "ats": "greenhouse", "greenhouse_id": "alphonso",     "url": "https://api.greenhouse.io/v1/boards/alphonso/jobs"},
    {"name": "Sprinklr India",           "ats": "greenhouse", "greenhouse_id": "sprinklr",     "url": "https://api.greenhouse.io/v1/boards/sprinklr/jobs"},
    {"name": "MoEngage",                 "ats": "greenhouse", "greenhouse_id": "moengage",     "url": "https://api.greenhouse.io/v1/boards/moengage/jobs"},
    {"name": "CleverTap",                "ats": "greenhouse", "greenhouse_id": "clevertap",    "url": "https://api.greenhouse.io/v1/boards/clevertap/jobs"},
    # NEW: AlphaSense — AI Engineer intern role
    # NOTE: possibly Greenhouse-backed; verify board slug before switching ats type
    {"name": "AlphaSense",               "ats": "playwright", "url": "https://www.alpha-sense.com/careers/"},
    # NEW: MiQ Digital
    # NOTE: possibly Greenhouse-backed; verify board slug before switching ats type
    {"name": "MiQ Digital",              "ats": "playwright", "url": "https://miqdigital.com/careers/"},
    # NEW: Zluri Technologies
    # NOTE: possibly Greenhouse-backed; verify board slug before switching ats type
    {"name": "Zluri Technologies",       "ats": "playwright", "url": "https://www.zluri.com/careers"},
    # NEW: Sarvam AI — Backend engineering / Gen AI roles both map here
    {"name": "Sarvam AI",                "ats": "playwright", "url": "https://www.sarvam.ai/careers"},
    # NEW: Frinks AI
    # NOTE: startup, domain unverified — confirm before deploying
    {"name": "Frinks AI",                "ats": "playwright", "url": "https://www.frinks.ai/careers"},
    # NEW: Potpie AI
    # NOTE: startup, domain unverified — confirm before deploying
    {"name": "Potpie AI",                "ats": "playwright", "url": "https://potpie.ai/careers"},
    # NEW: Cohortia AI
    # NOTE: startup, domain unverified — confirm before deploying
    {"name": "Cohortia AI",              "ats": "playwright", "url": "https://cohortia.ai/careers"},
    # NEW: Terafac Technologies — AI & Computer Vision
    # NOTE: domain unverified — confirm before deploying
    {"name": "Terafac Technologies",     "ats": "playwright", "url": "https://terafac.com/careers"},
    # NEW: Petasense Technologies
    {"name": "Petasense Technologies",   "ats": "playwright", "url": "https://www.petasense.com/careers"},
    # NEW: Morphing Machines
    # NOTE: domain unverified — confirm before deploying
    {"name": "Morphing Machines",        "ats": "playwright", "url": "https://www.morphingmachines.com/careers"},
    # NEW: Mowito Automation
    # NOTE: domain unverified — confirm before deploying
    {"name": "Mowito Automation",        "ats": "playwright", "url": "https://mowito.in/careers"},
    # NEW: Refroid Technologies
    # NOTE: domain unverified — confirm before deploying
    {"name": "Refroid Technologies",     "ats": "playwright", "url": "https://refroid.com/careers"},
    # NEW: Varaha ClimateAg — Android / Data Analyst / Frontend / Full-stack / MLOps / PM roles all map here
    # NOTE: domain unverified — confirm before deploying
    {"name": "Varaha ClimateAg",         "ats": "playwright", "url": "https://www.varaha.io/careers"},

    # ── IT Services / Consulting / GCC ────────────────────────────────────────
    {"name": "Infosys",                  "ats": "playwright", "url": "https://career.infosys.com/joblist?src=1&type=1"},
    {"name": "TCS",                      "ats": "playwright", "url": "https://ibegin.tcs.com/iBegin/faces/HomePage.xhtml"},
    {"name": "Wipro",                    "ats": "playwright", "url": "https://careers.wipro.com/careers-home/jobs?q={role}&location=India"},
    {"name": "HCL Tech",                 "ats": "playwright", "url": "https://www.hcltech.com/careers/search-jobs?keyword={role}&location=India"},
    {"name": "Cognizant",                "ats": "workday",    "url": "https://cognizant.wd1.myworkdayjobs.com/Cognizant_Careers/jobs?q={role}&locations=India"},
    # FIXED: was "workday" — accenture.com/in-en/careers is Accenture's own site,
    # not myworkdayjobs.com
    {"name": "Accenture",                "ats": "playwright", "url": "https://www.accenture.com/in-en/careers/jobsearch?jk={role}&cl=India"},
    {"name": "Capgemini",                "ats": "playwright", "url": "https://www.capgemini.com/in-en/careers/job-search/?q={role}&country=India"},
    {"name": "LTIMindtree",              "ats": "playwright", "url": "https://www.ltimindtree.com/careers/job-openings/?search={role}&location=India"},
    # NEW: EY GDS — Consulting (Industry 4.0-style engagements route through EY's general careers site)
    {"name": "EY GDS",                   "ats": "playwright", "url": "https://careers.ey.com/ey/search/?q={role}&location=India"},
    {"name": "KPMG India",               "ats": "playwright", "url": "https://kpmg.com/in/en/careers.html"},
    {"name": "UST Global",               "ats": "playwright", "url": "https://www.ust.com/en/careers"},
    {"name": "Manipal Technologies Limited","ats": "playwright","url": "https://www.manipaltechnologies.com/careers/"},
    {"name": "Human Powered Health (Quess Corp)","ats": "playwright","url": "https://www.quesscorp.com/careers/"},

    # ── Pharma / Healthcare / Life Sciences ──────────────────────────────────
    # NEW: Eli Lilly — Bengaluru
    # NOTE: widely believed to run on Workday; verify exact tenant before switching ats type
    {"name": "Eli Lilly",                "ats": "playwright", "url": "https://careers.lilly.com/us/en/search-results?keywords={role}&location=India"},
    # NEW: Pfizer Healthcare India — Data Science and general roles both map here
    # NOTE: widely believed to run on Workday; verify exact tenant before switching ats type
    {"name": "Pfizer Healthcare India",  "ats": "playwright", "url": "https://www.pfizer.com/about/careers"},
    # NEW: MSD Pharmaceuticals India (Merck)
    # NOTE: widely believed to run on Workday; verify exact tenant before switching ats type
    {"name": "MSD Pharmaceuticals India","ats": "playwright", "url": "https://jobs.msd.com/in/en/search-results?keywords={role}"},
    # NEW: Evernorth Health Services
    {"name": "Evernorth Health Services","ats": "playwright", "url": "https://jobs.evernorth.com/search-jobs?k={role}&l=India"},
    # NEW: Endpoint Clinical India
    {"name": "Endpoint Clinical India",  "ats": "playwright", "url": "https://www.endpointclinical.com/careers"},
    # NEW: Syneos Health — Gurugram
    {"name": "Syneos Health",            "ats": "playwright", "url": "https://careers.syneoshealth.com/search-jobs?k={role}&l=India"},
    # NEW: PharmaACE — Pune
    {"name": "PharmaACE",                "ats": "playwright", "url": "https://www.pharmaace.com/careers/"},
    # NEW: ClearView Healthcare Partners
    {"name": "ClearView Healthcare Partners","ats": "playwright","url": "https://clearviewhcp.com/careers/"},

    # ── Automotive / Aerospace / Industrial / Engineering ────────────────────
    # NEW: BMW Group India
    {"name": "BMW Group India",          "ats": "playwright", "url": "https://www.bmwgroup.jobs/in/en/search.html?query={role}"},
    # NEW: Mercedes-Benz Research & Development India
    {"name": "Mercedes-Benz R&D India",  "ats": "playwright", "url": "https://mbrdi.co.in/careers/"},
    # NEW: Triumph Motorcycles
    {"name": "Triumph Motorcycles",      "ats": "playwright", "url": "https://www.triumphmotorcycles.com/careers"},
    # NEW: VE Commercials (VE Commercial Vehicles)
    {"name": "VE Commercials",           "ats": "playwright", "url": "https://www.vecv.in/careers/"},
    # NEW: GE Aerospace — Bengaluru
    # NOTE: widely believed to run on Workday; verify exact tenant before switching ats type
    {"name": "GE Aerospace",             "ats": "playwright", "url": "https://jobs.gecareers.com/global/en/search-results?keywords={role}&location=India"},
    # NEW: GE Vernova Advanced — Bengaluru
    {"name": "GE Vernova",               "ats": "playwright", "url": "https://www.gevernova.com/careers/search-results?keywords={role}&location=India"},
    # NEW: Carrier Technologies India — AIML/Analytics, Electrical COE, MBD, Software COE roles all map here
    {"name": "Carrier Technologies India","ats": "playwright", "url": "https://careers.carrier.com/search-jobs?k={role}&l=India"},
    # NEW: Siemens EDA India (distinct legal entity from Siemens India — EDA/Mentor Graphics business)
    {"name": "Siemens EDA India",        "ats": "playwright", "url": "https://eda.sw.siemens.com/en-US/careers/"},
    # NEW: Arup India — Hyderabad
    {"name": "Arup India",               "ats": "playwright", "url": "https://www.arup.com/careers/search-and-apply?keywords={role}&location=India"},
    # NEW: Oceaneering International Services
    {"name": "Oceaneering International","ats": "playwright", "url": "https://www.oceaneering.com/careers/"},
    # NEW: Snivaa Consulting Engineers
    # NOTE: domain unverified — confirm before deploying
    {"name": "Snivaa Consulting Engineers","ats": "playwright","url": "https://snivaa.com/careers"},

    # ── Corporate / Business / Consulting / Other ────────────────────────────
    # NEW: Dentsu Global Services
    {"name": "Dentsu Global Services",    "ats": "playwright", "url": "https://www.dentsu.com/in/en/careers"},
    # NEW: Electronic Arts — AI Platform / Cloud Native Fullstack / Customer Platform / EADP roles all map here
    {"name": "Electronic Arts",           "ats": "playwright", "url": "https://ea.gcs-web.com/careers"},
    # NEW: Victoria's Secret — MBA Business Analytics
    {"name": "Victoria's Secret",         "ats": "playwright", "url": "https://www.victoriassecretandco.com/careers"},
    # NEW: Red Nucleus
    {"name": "Red Nucleus",               "ats": "playwright", "url": "https://rednucleus.com/careers/"},
    # NEW: Pegasystems — Hyderabad
    {"name": "Pegasystems",               "ats": "playwright", "url": "https://www.pega.com/about/careers/search?keywords={role}&location=India"},
    # NEW: STN 10xscale Technology — EdTech / Healthcare & AI roles both map here
    # NOTE: domain unverified — confirm before deploying
    {"name": "STN 10xscale Technology",   "ats": "playwright", "url": "https://10xscale.ai/careers"},
    # NEW: Futures First Info Services — Market Analyst / Quant Research roles both map here
    {"name": "Futures First Info Services","ats": "playwright","url": "https://www.futuresfirst.com/careers/"},
    # NEW: MBB Labs (Maybank)
    # NOTE: may route through Maybank's regional careers portal — domain unverified
    {"name": "MBB Labs (Maybank)",        "ats": "playwright", "url": "https://www.maybank.com/en/careers.page"},
    # NEW: Hexalog Technologies
    # NOTE: domain unverified — confirm before deploying
    {"name": "Hexalog Technologies",      "ats": "playwright", "url": "https://hexalog.tech/careers"},
    # NEW: Trisim Technologies
    # NOTE: domain unverified — confirm before deploying
    {"name": "Trisim Technologies",       "ats": "playwright", "url": "https://trisim.tech/careers"},
    # NEW: ValetEZ — Electronics, Inside Sales
    # NOTE: domain unverified — confirm before deploying
    {"name": "ValetEZ",                   "ats": "playwright", "url": "https://valetez.com/careers"},
    # NEW: CloudFiles Technologies — IT and Non-IT roles both map here
    # NOTE: domain unverified — confirm before deploying
    {"name": "CloudFiles Technologies",   "ats": "playwright", "url": "https://cloudfilestech.com/careers"},
    # NEW: Critical Path Technologies (SalarySe) — Product
    {"name": "Critical Path Technologies (SalarySe)","ats": "playwright","url": "https://salaryse.com/careers"},
    # NEW: Ozi Technologies — Category/Ops, Founder's Office, Growth/Brand, Product roles all map here
    # NOTE: no confidently identifiable public domain found — confirm the correct
    # entity/URL with the placement cell before adding a live scraper
    {"name": "Ozi Technologies",          "ats": "playwright", "url": ""},
    # NEW: Intelenergi Global — Analytical Research, IT/AI, Power Electronics, GTM Strategy roles all map here
    # NOTE: no confidently identifiable public domain found — confirm with placement cell
    {"name": "Intelenergi Global",        "ats": "playwright", "url": ""},
    # NEW: Global Innovation Hub — PM/Business Analysis, UI/UX/App Dev, AI/ML/App Dev roles all map here
    # NOTE: no confidently identifiable public domain found — confirm with placement cell
    {"name": "Global Innovation Hub",     "ats": "playwright", "url": ""},
    # NEW: ARKS Ventures — Non Tech
    # NOTE: domain unverified — confirm before deploying
    {"name": "ARKS Ventures",             "ats": "playwright", "url": ""},
    # NEW: FSR Global Council — Smart Grid Data Analysis
    # NOTE: domain unverified — confirm before deploying
    {"name": "FSR Global Council",        "ats": "playwright", "url": ""},
    # NEW: Clarity
    # NOTE: name is too generic to confidently resolve to a specific company/domain —
    # confirm the exact entity with the placement cell before adding a scraper
    {"name": "Clarity",                   "ats": "playwright", "url": ""},

    # ══════════════════════════════════════════════════════════════════════════
    # ── God Tier — Quant / HFT ────────────────────────────────────────────────
    # CONFIRMED live: custom career site, not on a public ATS API
    {"name": "Renaissance Technologies",  "ats": "playwright", "url": "https://www.rentec.com/Careers.action?jobs=true"},
    # NOTE: domain is the real firm site; exact careers path unverified — confirm before deploying
    {"name": "Radix Trading",             "ats": "playwright", "url": "https://www.radixtrading.co/careers"},
    # NOTE: domain unverified — confirm before deploying
    {"name": "TGS Management",            "ats": "playwright", "url": "https://www.tgsmanagement.com/careers"},
    # NOTE: domain unverified — confirm before deploying
    {"name": "Arrowstreet Capital",       "ats": "playwright", "url": "https://www.arrowstreetcapital.com/careers"},
    # NOTE: domain unverified — confirm before deploying
    {"name": "PDT Partners",              "ats": "playwright", "url": "https://www.pdtpartners.com/careers"},

    # ── SSS Tier — Quant / HFT ────────────────────────────────────────────────
    # CONFIRMED live: custom career site, not on a public ATS API
    {"name": "Citadel",                   "ats": "playwright", "url": "https://www.citadel.com/careers/"},
    # CONFIRMED live: custom career site, not on a public ATS API
    {"name": "Point72",                   "ats": "playwright", "url": "https://careers.point72.com/"},
    # CONFIRMED live: custom career site, not on a public ATS API
    {"name": "Hudson River Trading",      "ats": "playwright", "url": "https://www.hudsonrivertrading.com/careers/"},
    # NOTE: domain unverified — confirm before deploying
    {"name": "Jump Trading",              "ats": "playwright", "url": "https://www.jumptrading.com/careers/"},
    # NOTE: could not confidently identify this as a real, distinct quant firm — this
    # name does not appear in industry firm lists alongside the others in this tier;
    # please double check the intended company name before adding a live scraper
    {"name": "Ridgewater Capital",        "ats": "playwright", "url": ""},
    # NOTE: domain unverified — confirm before deploying
    {"name": "Quadrature Capital",        "ats": "playwright", "url": "https://www.quadrature.ai/careers"},

    # ── SS Tier — Quant / HFT ─────────────────────────────────────────────────
    # CONFIRMED live: custom career site, not on a public ATS API
    {"name": "Optiver",                   "ats": "playwright", "url": "https://www.optiver.com/join-us/jobs"},
    # CONFIRMED live: custom career site, not on a public ATS API
    {"name": "Two Sigma",                 "ats": "playwright", "url": "https://careers.twosigma.com/"},
    # CONFIRMED live: custom career site, not on a public ATS API
    {"name": "D.E. Shaw",                 "ats": "playwright", "url": "https://www.deshaw.com/careers"},
    # NOTE: domain unverified — confirm before deploying
    {"name": "Five Rings",                "ats": "playwright", "url": "https://www.fiveringscapital.com/careers"},
    # NOTE: domain unverified — confirm before deploying
    {"name": "Voleon",                    "ats": "playwright", "url": "https://voleon.com/careers/"},
    # NOTE: domain unverified — confirm before deploying
    {"name": "XTX Markets",               "ats": "playwright", "url": "https://www.xtxmarkets.com/careers/"},
    # NOTE: widely known as "Susquehanna International Group (SIG)"; domain
    # unverified exact careers path — confirm before deploying
    {"name": "Susquehanna (SIG)",         "ats": "playwright", "url": "https://careers.sig.com/"},

    # ── SS- Tier — Quant / HFT ────────────────────────────────────────────────
    # NOTE: domain unverified — confirm before deploying
    {"name": "IMC Trading",               "ats": "playwright", "url": "https://careers.imc.com/global/en"},
    # CONFIRMED: DRW is genuinely Greenhouse-backed
    {"name": "DRW",                       "ats": "greenhouse", "greenhouse_id": "drweng",       "url": "https://api.greenhouse.io/v1/boards/drweng/jobs"},
    # NOTE: domain unverified — confirm before deploying
    {"name": "Virtu Financial",           "ats": "playwright", "url": "https://www.virtu.com/careers/"},
    # NOTE: domain unverified — confirm before deploying
    {"name": "Maven Securities",          "ats": "playwright", "url": "https://www.mavensecurities.com/careers"},
    # NOTE: domain unverified — confirm before deploying
    {"name": "Millennium",                "ats": "playwright", "url": "https://www.millennium.com/careers"},
    # NOTE: domain unverified — confirm before deploying
    {"name": "AQR Capital",               "ats": "playwright", "url": "https://www.aqr.com/Careers"},
    # NOTE: domain unverified — confirm before deploying
    {"name": "G-Research",                "ats": "playwright", "url": "https://www.gresearch.com/careers/"},

    # ── S Tier ────────────────────────────────────────────────────────────────
    # NOTE: domain unverified — confirm before deploying
    {"name": "WorldQuant",                "ats": "playwright", "url": "https://www.worldquant.com/careers/"},
    # NOTE: domain unverified — confirm before deploying
    {"name": "Squarepoint Capital",       "ats": "playwright", "url": "https://www.squarepoint-capital.com/careers"},
    # CONFIRMED live: custom career site, not on a public ATS API
    {"name": "Akuna Capital",             "ats": "playwright", "url": "https://akunacapital.com/careers/"},
    # NOTE: domain unverified — confirm before deploying
    {"name": "Flow Traders",              "ats": "playwright", "url": "https://www.flowtraders.com/careers"},
    # NOTE: widely believed to be Greenhouse-backed; board slug unverified — confirm
    # before switching ats type
    {"name": "Anthropic",                 "ats": "playwright", "url": "https://www.anthropic.com/careers"},
    # NOTE: OpenAI's careers site is not on the classic Greenhouse/Lever API pattern —
    # confirm exact ATS before switching ats type
    {"name": "OpenAI",                    "ats": "playwright", "url": "https://openai.com/careers/"},
    {"name": "Netflix",                   "ats": "playwright", "url": "https://explore.jobs.netflix.net/careers"},
    # NOTE: widely believed to be Greenhouse-backed; board slug unverified — confirm
    # before switching ats type
    {"name": "Roblox",                    "ats": "playwright", "url": "https://careers.roblox.com/jobs"},

    # ── A+ Tier ───────────────────────────────────────────────────────────────
    # NOTE: widely believed to be Greenhouse-backed; board slug unverified — confirm
    # before switching ats type
    {"name": "Duolingo",                  "ats": "playwright", "url": "https://careers.duolingo.com/"},
    {"name": "Block (Square)",            "ats": "playwright", "url": "https://block.xyz/careers"},
    {"name": "Tesla",                     "ats": "playwright", "url": "https://www.tesla.com/careers/search/?query={role}&region=India"},
    # NOTE: widely believed to be Greenhouse-backed; board slug unverified — confirm
    # before switching ats type
    {"name": "DoorDash",                  "ats": "playwright", "url": "https://careers.doordash.com/"},

    # ── A Tier ────────────────────────────────────────────────────────────────
    # NOTE: widely believed to be Greenhouse-backed; board slug unverified — confirm
    # before switching ats type
    {"name": "Asana",                     "ats": "playwright", "url": "https://asana.com/jobs"},
    # NOTE: widely believed to be Greenhouse-backed; board slug unverified — confirm
    # before switching ats type
    {"name": "Datadog",                   "ats": "playwright", "url": "https://careers.datadoghq.com/"},
    {"name": "Snap",                      "ats": "playwright", "url": "https://careers.snap.com/jobs"},
    # NOTE: possibly Greenhouse or Ashby-backed; unverified — confirm before switching ats type
    {"name": "Ramp",                      "ats": "playwright", "url": "https://ramp.com/careers"},
    {"name": "Spotify",                   "ats": "playwright", "url": "https://www.lifeatspotify.com/jobs"},
    # NOTE: widely believed to be Greenhouse-backed; board slug unverified — confirm
    # before switching ats type
    {"name": "Dropbox",                   "ats": "playwright", "url": "https://dropbox.com/jobs"},
    # NOTE: widely believed to be Greenhouse-backed; board slug unverified — confirm
    # before switching ats type
    {"name": "Pinterest",                 "ats": "playwright", "url": "https://www.pinterestcareers.com/"},
    # NOTE: widely believed to be Greenhouse-backed; board slug unverified — confirm
    # before switching ats type
    {"name": "Plaid",                     "ats": "playwright", "url": "https://plaid.com/careers/"},
    # NOTE: widely believed to be Greenhouse-backed; board slug unverified — confirm
    # before switching ats type
    {"name": "Figma",                     "ats": "playwright", "url": "https://www.figma.com/careers/"},
    # NOTE: widely believed to be Greenhouse-backed; board slug unverified — confirm
    # before switching ats type
    {"name": "Discord",                   "ats": "playwright", "url": "https://discord.com/careers"},
    # NOTE: widely believed to be Greenhouse-backed; board slug unverified — confirm
    # before switching ats type
    {"name": "Robinhood",                 "ats": "playwright", "url": "https://careers.robinhood.com/"},
    {"name": "C3.ai",                     "ats": "playwright", "url": "https://c3.ai/careers/"},

    # ── B+ Tier ───────────────────────────────────────────────────────────────
    {"name": "Blackstone",                "ats": "playwright", "url": "https://www.blackstone.com/careers/"},
    {"name": "eBay",                      "ats": "playwright", "url": "https://ebaycareers.com/"},
    # NOTE: widely believed to use Ashby, not Greenhouse — confirm before switching
    # ats type
    {"name": "xAI",                       "ats": "playwright", "url": "https://x.ai/careers"},
    # NOTE: widely believed to be Greenhouse-backed; board slug unverified — confirm
    # before switching ats type
    {"name": "GitHub",                    "ats": "playwright", "url": "https://github.careers/"},
    {"name": "Palantir",                  "ats": "playwright", "url": "https://www.palantir.com/careers/"},
    {"name": "Lyft",                      "ats": "playwright", "url": "https://www.lyft.com/careers"},
    # NOTE: Twitch is Amazon-owned and hiring routes through amazon.jobs
    {"name": "Twitch",                    "ats": "playwright", "url": "https://www.amazon.jobs/en/teams/Twitch"},

    # ── B Tier ────────────────────────────────────────────────────────────────
    {"name": "Capital One",               "ats": "playwright", "url": "https://www.capitalonecareers.com/"},
    {"name": "Intel",                     "ats": "playwright", "url": "https://jobs.intel.com/en/search-jobs"},

    # ── B- Tier ───────────────────────────────────────────────────────────────
    {"name": "Wells Fargo",               "ats": "playwright", "url": "https://www.wellsfargojobs.com/"},
    {"name": "Bank of America",           "ats": "playwright", "url": "https://careers.bankofamerica.com/"},
    {"name": "Boeing",                    "ats": "playwright", "url": "https://jobs.boeing.com/"},
    {"name": "Booz Allen Hamilton",       "ats": "playwright", "url": "https://careers.boozallen.com/"},
    {"name": "Arrow Electronics",         "ats": "playwright", "url": "https://careers.arrow.com/"},

    # ══════════════════════════════════════════════════════════════════════════
    # ── Revision 3 (July 19, 2026) — user's follow-up batch ─────────────────────
    # CONFIRMED live via search
    {"name": "SLB",                       "ats": "playwright", "url": "https://apply.slb.com/careers/profile"},
    {"name": "Koch Industries",           "ats": "playwright", "url": "https://jobs.kochcareers.com/en/search/jobs/in/country/india"},
    {"name": "Autodesk",                  "ats": "playwright", "url": "https://www.autodesk.com/careers/search-jobs?location=India"},
    # CONFIRMED live — TrueFirms is a B2B IT staff-augmentation marketplace, not a
    # typical employer with an internal jobs board; listed here as requested but
    # note it functions more like a staffing/agency directory than a direct employer
    {"name": "TrueFirms",                 "ats": "playwright", "url": "https://www.truefirms.co/jobs"},
    # NOTE: "carousel" is too generic to confidently resolve to one company (could be
    # Carousell, the Singapore marketplace, or something else entirely) — flagged
    # rather than guessed; confirm the exact company before deploying
    {"name": "Carousel (unconfirmed)",    "ats": "playwright", "url": ""},
    # NOTE: "emergent" is too generic to confidently resolve (Emergent BioSolutions?
    # a specific startup named Emergent?) — flagged rather than guessed
    {"name": "Emergent (unconfirmed)",    "ats": "playwright", "url": ""},
    {"name": "Emerson",                   "ats": "playwright", "url": "https://www.emerson.com/en/corporate/careers"},
    # CONFIRMED live — YC-backed options-trading backtester, Indian retail-trader focus
    {"name": "AlgoTest",                  "ats": "playwright", "url": "https://algotest.in/careers"},
    # NOTE: could not confidently identify a company literally named "Brocolli" —
    # flagged with an empty URL rather than guessed; please double-check this name
    {"name": "Brocolli (unconfirmed)",    "ats": "playwright", "url": ""},
    # NOTE: there's a "Matiks" (Internshala-listed, no live openings at time of
    # writing) and an unrelated "Matik" (US-based, data/AI reporting tool) — these
    # are two different companies with similar names; using the Indian "Matiks"
    # since that matches the context of your other additions, but please confirm
    {"name": "Matiks",                    "ats": "playwright", "url": ""},
    {"name": "Trellix",                   "ats": "playwright", "url": "https://www.trellix.com/about/careers/"},
    {"name": "Lowe's India",              "ats": "playwright", "url": "https://talent.lowes.com/us/en/lowes-india"},
    {"name": "Wingify",                   "ats": "playwright", "url": "https://wingify.com/careers/"},
    # NOTE: "layer up" is too generic to confidently resolve to one company —
    # flagged rather than guessed; confirm the exact company name
    {"name": "Layer Up (unconfirmed)",    "ats": "playwright", "url": ""},
    {"name": "Nike",                      "ats": "playwright", "url": "https://jobs.nike.com/?location=India"},
    {"name": "Honeywell",                 "ats": "playwright", "url": "https://careers.honeywell.com/us/en/search-results?location=India"},
    # CONFIRMED live — Redrob is a Seoul/Delhi/Mumbai/NY LLM-application startup;
    # official company domain unverified, using the Wellfound listing as the source
    {"name": "Redrob",                    "ats": "playwright", "url": "https://wellfound.com/company/redrobofficial/jobs"},
    # NOTE: "Milestone" is too generic (Milestone Systems? a different firm?) —
    # flagged rather than guessed; confirm the exact company name
    {"name": "Milestone (unconfirmed)",   "ats": "playwright", "url": ""},
    {"name": "Redis",                     "ats": "playwright", "url": "https://redis.io/careers/"},
    {"name": "Red Hat",                   "ats": "playwright", "url": "https://www.redhat.com/en/jobs"},
]
