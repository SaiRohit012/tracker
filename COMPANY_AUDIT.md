# Company source audit

Checked 19 September 2026 (India time). These are point-in-time HTTP/schema checks, not proof that every job is collected. The updated registry contains 329 entries, including 13 disabled placeholders.

- reachable_unverified: 133
- failed: 128
- api_responding: 43
- blocked: 12
- disabled: 13

API responses still need correct ownership and complete extraction. Reachable custom pages require dedicated parser verification. Blocks and network failures may depend on execution environment.

| Company | Adapter | Check result | Detail |
|---|---|---|---|
| Google India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Amazon / AWS | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Microsoft India | playwright | failed | ConnectionError: HTTPSConnectionPool(host='jobs.microsoft.com', port=443): Max retries exceeded with url: /en/us/search?q=engineer&lc=India (Caused by NameResolutionError("HTTPSConnection(host='jobs.microsoft.com', port=443): Failed to resolve 'jobs.microsoft.com' ([Errno 11001] getaddrinfo failed)" |
| Meta India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Apple India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Adobe India | workday | api_responding | Schema checked; confirm official ownership and run full collection |
| Nvidia India | workday | api_responding | Schema checked; confirm official ownership and run full collection |
| Qualcomm India | workday | failed | HTTP 422 |
| LinkedIn India | playwright | failed | HTTP 404 |
| Walmart Global Tech | workday | failed | HTTP 422 |
| MediaTek India | playwright | failed | HTTP 404 |
| Micron Technology | workday | api_responding | Schema checked; confirm official ownership and run full collection |
| ByteDance India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Akamai India | workday | failed | HTTP 422 |
| Airbnb India | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Coupang India | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Zalando India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| LG Ad Solutions India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Wayfair India | greenhouse | failed | HTTP 404 |
| AMD India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| ARM Embedded Technologies | playwright | failed | HTTP 404 |
| Marvell Technology | playwright | failed | ConnectionError: HTTPSConnectionPool(host='careers.marvell.com', port=443): Max retries exceeded with url: /search-results?keywords=engineer&location=India (Caused by NameResolutionError("HTTPSConnection(host='careers.marvell.com', port=443): Failed to resolve 'careers.marvell.com' ([Errno 11001] ge |
| NXP India | playwright | failed | HTTP 404 |
| Onsemi | playwright | blocked | HTTP 403 |
| Skyworks Solutions | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Western Digital | playwright | failed | HTTP 404 |
| Microchip Technology | playwright | blocked | HTTP 403 |
| Infineon Technologies India | playwright | failed | HTTP 404 |
| Astera Labs | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Goldman Sachs India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| JP Morgan India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Morgan Stanley India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| D.E. Shaw India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Jane Street India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Tower Research Capital | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Arcesium | greenhouse | failed | HTTP 404 |
| Bloomberg India | playwright | blocked | HTTP 403 |
| BlackRock India | workday | failed | HTTP 404 |
| Visa India | workday | api_responding | Schema checked; confirm official ownership and run full collection |
| HSBC Tech India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Zeta | greenhouse | failed | HTTP 404 |
| Societe Generale India | playwright | failed | HTTP 404 |
| Barclays India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Citi India | workday | failed | HTTP 404 |
| Kotak Mahindra Bank | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Kotak Securities | playwright | failed | HTTP 404 |
| Coinbase India | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Deutsche Bank India | workday | api_responding | Schema checked; confirm official ownership and run full collection |
| American Express India | playwright | failed | ConnectionError: HTTPSConnectionPool(host='jobs.americanexpress.com', port=443): Max retries exceeded with url: /india/jobs?q=engineer (Caused by NameResolutionError("HTTPSConnection(host='jobs.americanexpress.com', port=443): Failed to resolve 'jobs.americanexpress.com' ([Errno 11001] getaddrinfo f |
| Fidelity Investments India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Mastercard India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Equifax India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Moody's Analytics | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Morningstar India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| MSCI Services | playwright | failed | HTTP 404 |
| Synchrony | playwright | failed | SSLError: HTTPSConnectionPool(host='synchronycareers.com', port=443): Max retries exceeded with url: /search-jobs?k=engineer&l=India (Caused by SSLError(SSLError(1, '[SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:1010)'))) |
| Swiss Re GBS India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Stripe India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| PayPal India | workday | api_responding | Schema checked; confirm official ownership and run full collection |
| Razorpay | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Intuit India | workday | blocked | HTTP 401 |
| Rippling India | greenhouse | failed | HTTP 404 |
| PhonePe | lever | failed | HTTP 404 |
| Zerodha | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Groww | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| CoinSwitch | lever | failed | HTTP 404 |
| Yubi | lever | failed | HTTP 404 |
| Slice | lever | failed | HTTP 404 |
| smallcase | greenhouse | failed | HTTP 404 |
| Jeeves | greenhouse | failed | HTTP 404 |
| Khatabook | greenhouse | failed | HTTP 404 |
| Progcap | greenhouse | failed | HTTP 404 |
| mPokket | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Simpl | greenhouse | failed | HTTP 404 |
| Finicity | workday | failed | HTTP 404 |
| Paytm | lever | api_responding | Schema checked; confirm official ownership and run full collection |
| Blackhawk Network India | lever | failed | HTTP 404 |
| super.money | playwright | failed | HTTP 404 |
| Navi Technologies | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Prosperr.io | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Scapia Technology | playwright | failed | SSLError: HTTPSConnectionPool(host='www.scapia.club', port=443): Max retries exceeded with url: /careers (Caused by SSLError(SSLCertVerificationError(1, "[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'www.scapia.club'. (_ssl.c:1010)"))) |
| Stampmyvisa | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Svamaan Financial Services | playwright | failed | ConnectTimeout: HTTPSConnectionPool(host='svamaan.com', port=443): Max retries exceeded with url: /careers (Caused by ConnectTimeoutError(<HTTPSConnection(host='svamaan.com', port=443) at 0x259ad9d1760>, 'Connection to svamaan.com timed out. (connect timeout=8)')) |
| Rubrik India | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Cisco India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| IBM India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Oracle India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Juniper Networks India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Netskope India | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Confluent India | greenhouse | failed | HTTP 404 |
| ServiceNow India | playwright | failed | HTTP 404 |
| Databricks India | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Snowflake India | greenhouse | failed | HTTP 404 |
| GitLab India | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Palo Alto Networks India | playwright | failed | HTTP 404 |
| Uptycs | greenhouse | failed | HTTP 404 |
| Fortanix | greenhouse | failed | HTTP 404 |
| Safe Security | greenhouse | failed | HTTP 404 |
| Teradata India | workday | blocked | HTTP 401 |
| Hyland India | playwright | failed | HTTP 404 |
| Siemens India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Experian India | workday | failed | HTTP 422 |
| DocuSign India | greenhouse | failed | HTTP 404 |
| Elastic India | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| MongoDB India | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Cloudflare India | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Twilio India | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Samsara India | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Redwood Software | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Orange Business India | playwright | failed | ConnectionError: HTTPSConnectionPool(host='careers.orange-business.com', port=443): Max retries exceeded with url: / (Caused by NameResolutionError("HTTPSConnection(host='careers.orange-business.com', port=443): Failed to resolve 'careers.orange-business.com' ([Errno 11001] getaddrinfo failed)")) |
| Flipkart | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Swiggy | lever | failed | HTTP 404 |
| Zomato | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Freshworks | greenhouse | failed | HTTP 404 |
| Zoho | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Atlassian India | greenhouse | failed | HTTP 404 |
| Meesho | lever | api_responding | Schema checked; confirm official ownership and run full collection |
| CRED | lever | failed | HTTP 404 |
| Zepto | lever | failed | HTTP 404 |
| Dream11 | playwright | failed | ConnectionError: HTTPSConnectionPool(host='careers.dream11.com', port=443): Max retries exceeded with url: / (Caused by NameResolutionError("HTTPSConnection(host='careers.dream11.com', port=443): Failed to resolve 'careers.dream11.com' ([Errno 11001] getaddrinfo failed)")) |
| Ola / Ola Electric | playwright | failed | ConnectionError: HTTPSConnectionPool(host='careers.ola.com', port=443): Max retries exceeded with url: /jobs?q=engineer (Caused by NameResolutionError("HTTPSConnection(host='careers.ola.com', port=443): Failed to resolve 'careers.ola.com' ([Errno 11001] getaddrinfo failed)")) |
| PolicyBazaar | playwright | failed | ConnectionError: HTTPSConnectionPool(host='jobs.policybazaar.com', port=443): Max retries exceeded with url: / (Caused by NameResolutionError("HTTPSConnection(host='jobs.policybazaar.com', port=443): Failed to resolve 'jobs.policybazaar.com' ([Errno 11001] getaddrinfo failed)")) |
| Uber India | playwright | failed | HTTP 406 |
| Booking.com India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Agoda India | playwright | failed | HTTP 404 |
| Curefit | greenhouse | failed | HTTP 404 |
| Notion India | ashby | api_responding | Schema checked; confirm official ownership and run full collection |
| Warner Bros Discovery | workday | api_responding | Schema checked; confirm official ownership and run full collection |
| MakeMyTrip | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| InMobi | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Nykaa Tech | playwright | failed | HTTP 404 |
| Cars24 | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Myntra | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| ShareChat | greenhouse | failed | HTTP 404 |
| Urban Company | greenhouse | failed | HTTP 404 |
| Cleartrip | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Delhivery | playwright | failed | ConnectionError: HTTPSConnectionPool(host='careers.delhivery.com', port=443): Max retries exceeded with url: /jobs?q=engineer (Caused by NameResolutionError("HTTPSConnection(host='careers.delhivery.com', port=443): Failed to resolve 'careers.delhivery.com' ([Errno 11001] getaddrinfo failed)")) |
| Lenskart | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Netradyne | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| OfBusiness | playwright | failed | HTTP 406 |
| Spinny | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Virgio | playwright | failed | HTTP 404 |
| Zetwerk | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Dashverse | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Teleparty | playwright | failed | HTTP 404 |
| Juspay | greenhouse | failed | HTTP 404 |
| Atlan | ashby | api_responding | Schema checked; confirm official ownership and run full collection |
| Instabase | greenhouse | failed | HTTP 404 |
| Yellow.ai | lever | failed | HTTP 404 |
| Hevo Data | lever | api_responding | Schema checked; confirm official ownership and run full collection |
| Observe.AI | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Harness | greenhouse | failed | HTTP 404 |
| Plivo | greenhouse | failed | HTTP 404 |
| LambdaTest | lever | failed | HTTP 404 |
| Multiplier | greenhouse | failed | HTTP 404 |
| Simpplr | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Pixis | greenhouse | failed | HTTP 404 |
| Moveworks | greenhouse | failed | HTTP 404 |
| Sigmoid | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Tenstorrent | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| DataWeave | greenhouse | failed | HTTP 404 |
| Contentstack | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Builder.ai | greenhouse | failed | HTTP 404 |
| SaaS Labs | greenhouse | failed | HTTP 404 |
| Seclore | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Catchpoint | greenhouse | failed | HTTP 404 |
| HackerEarth | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Postman | greenhouse | failed | HTTP 404 |
| BrowserStack | workday | api_responding | Schema checked; confirm official ownership and run full collection |
| Chargebee | greenhouse | failed | HTTP 404 |
| Darwinbox | greenhouse | failed | HTTP 404 |
| Whatfix | greenhouse | failed | HTTP 404 |
| Salesforce India | workday | api_responding | Schema checked; confirm official ownership and run full collection |
| Alphonso | greenhouse | failed | HTTP 404 |
| Sprinklr India | greenhouse | failed | HTTP 404 |
| MoEngage | greenhouse | failed | HTTP 404 |
| CleverTap | greenhouse | failed | HTTP 404 |
| AlphaSense | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| MiQ Digital | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Zluri Technologies | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Sarvam AI | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Frinks AI | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Potpie AI | playwright | failed | HTTP 404 |
| Cohortia AI | playwright | failed | HTTP 404 |
| Terafac Technologies | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Petasense Technologies | playwright | failed | SSLError: HTTPSConnectionPool(host='www.petasense.com', port=443): Max retries exceeded with url: /careers (Caused by SSLError(SSLCertVerificationError(1, "[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'www.petasense.com'. (_ssl.c:1010)") |
| Morphing Machines | playwright | failed | HTTP 404 |
| Mowito Automation | playwright | failed | HTTP 404 |
| Refroid Technologies | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Varaha ClimateAg | playwright | failed | ConnectionError: HTTPSConnectionPool(host='www.varaha.io', port=443): Max retries exceeded with url: /careers (Caused by NameResolutionError("HTTPSConnection(host='www.varaha.io', port=443): Failed to resolve 'www.varaha.io' ([Errno 11001] getaddrinfo failed)")) |
| Infosys | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| TCS | playwright | failed | ConnectionError: HTTPSConnectionPool(host='ibegin.tcs.com', port=443): Max retries exceeded with url: /iBegin/faces/HomePage.xhtml (Caused by NameResolutionError("HTTPSConnection(host='ibegin.tcs.com', port=443): Failed to resolve 'ibegin.tcs.com' ([Errno 11001] getaddrinfo failed)")) |
| Wipro | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| HCL Tech | playwright | failed | HTTP 404 |
| Cognizant | workday | failed | HTTP 422 |
| Accenture | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Capgemini | playwright | failed | HTTP 404 |
| LTIMindtree | playwright | failed | HTTP 406 |
| EY GDS | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| KPMG India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| UST Global | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Manipal Technologies Limited | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Human Powered Health (Quess Corp) | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Eli Lilly | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Pfizer Healthcare India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| MSD Pharmaceuticals India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Evernorth Health Services | playwright | failed | ConnectionError: HTTPSConnectionPool(host='jobs.evernorth.com', port=443): Max retries exceeded with url: /search-jobs?k=engineer&l=India (Caused by NameResolutionError("HTTPSConnection(host='jobs.evernorth.com', port=443): Failed to resolve 'jobs.evernorth.com' ([Errno 11001] getaddrinfo failed)")) |
| Endpoint Clinical India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Syneos Health | playwright | failed | ConnectionError: HTTPSConnectionPool(host='careers.syneoshealth.com', port=443): Max retries exceeded with url: /search-jobs?k=engineer&l=India (Caused by NameResolutionError("HTTPSConnection(host='careers.syneoshealth.com', port=443): Failed to resolve 'careers.syneoshealth.com' ([Errno 11001] geta |
| PharmaACE | playwright | failed | HTTP 404 |
| ClearView Healthcare Partners | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| BMW Group India | playwright | failed | ConnectionError: HTTPSConnectionPool(host='www.bmwgroup.jobs', port=443): Max retries exceeded with url: /in/en/search.html?query=engineer (Caused by ReadTimeoutError("HTTPSConnectionPool(host='www.bmwgroup.jobs', port=443): Read timed out. (read timeout=15)")) |
| Mercedes-Benz R&D India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Triumph Motorcycles | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| VE Commercials | playwright | blocked | HTTP 403 |
| GE Aerospace | playwright | failed | ConnectionError: HTTPSConnectionPool(host='jobs.gecareers.com', port=443): Max retries exceeded with url: /global/en/search-results?keywords=engineer&location=India (Caused by NameResolutionError("HTTPSConnection(host='jobs.gecareers.com', port=443): Failed to resolve 'jobs.gecareers.com' ([Errno 11 |
| GE Vernova | playwright | failed | HTTP 404 |
| Carrier Technologies India | playwright | failed | HTTP 400 |
| Siemens EDA India | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Arup India | playwright | failed | HTTP 404 |
| Oceaneering International | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Snivaa Consulting Engineers | playwright | failed | ConnectionError: HTTPSConnectionPool(host='snivaa.com', port=443): Max retries exceeded with url: /careers (Caused by NameResolutionError("HTTPSConnection(host='snivaa.com', port=443): Failed to resolve 'snivaa.com' ([Errno 11001] getaddrinfo failed)")) |
| Dentsu Global Services | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Electronic Arts | playwright | failed | ConnectionError: HTTPSConnectionPool(host='ea.gcs-web.com', port=443): Max retries exceeded with url: /careers (Caused by NameResolutionError("HTTPSConnection(host='ea.gcs-web.com', port=443): Failed to resolve 'ea.gcs-web.com' ([Errno 11001] getaddrinfo failed)")) |
| Victoria's Secret | playwright | failed | ConnectionError: HTTPSConnectionPool(host='www.victoriassecretandco.com', port=443): Max retries exceeded with url: /careers (Caused by ReadTimeoutError("HTTPSConnectionPool(host='www.victoriassecretandco.com', port=443): Read timed out. (read timeout=15)")) |
| Red Nucleus | playwright | failed | RetryError: HTTPSConnectionPool(host='rednucleus.com', port=443): Max retries exceeded with url: /careers/ (Caused by ResponseError('too many 429 error responses')) |
| Pegasystems | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| STN 10xscale Technology | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Futures First Info Services | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| MBB Labs (Maybank) | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Hexalog Technologies | playwright | failed | ConnectionError: HTTPSConnectionPool(host='hexalog.tech', port=443): Max retries exceeded with url: /careers (Caused by NameResolutionError("HTTPSConnection(host='hexalog.tech', port=443): Failed to resolve 'hexalog.tech' ([Errno 11001] getaddrinfo failed)")) |
| Trisim Technologies | playwright | failed | ConnectionError: HTTPSConnectionPool(host='trisim.tech', port=443): Max retries exceeded with url: /careers (Caused by NameResolutionError("HTTPSConnection(host='trisim.tech', port=443): Failed to resolve 'trisim.tech' ([Errno 11001] getaddrinfo failed)")) |
| ValetEZ | playwright | failed | HTTP 404 |
| CloudFiles Technologies | playwright | failed | ConnectionError: HTTPSConnectionPool(host='cloudfilestech.com', port=443): Max retries exceeded with url: /careers (Caused by NameResolutionError("HTTPSConnection(host='cloudfilestech.com', port=443): Failed to resolve 'cloudfilestech.com' ([Errno 11001] getaddrinfo failed)")) |
| Critical Path Technologies (SalarySe) | playwright | failed | HTTP 404 |
| Ozi Technologies | playwright | disabled | Placeholder: needs verified official URL |
| Intelenergi Global | playwright | disabled | Placeholder: needs verified official URL |
| Global Innovation Hub | playwright | disabled | Placeholder: needs verified official URL |
| ARKS Ventures | playwright | disabled | Placeholder: needs verified official URL |
| FSR Global Council | playwright | disabled | Placeholder: needs verified official URL |
| Clarity | playwright | disabled | Placeholder: needs verified official URL |
| Renaissance Technologies | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Radix Trading | playwright | failed | HTTP 404 |
| TGS Management | playwright | failed | ConnectTimeout: HTTPSConnectionPool(host='www.tgsmanagement.com', port=443): Max retries exceeded with url: /careers (Caused by ConnectTimeoutError(<HTTPSConnection(host='www.tgsmanagement.com', port=443) at 0x259ad9eb470>, 'Connection to www.tgsmanagement.com timed out. (connect timeout=8)')) |
| Arrowstreet Capital | playwright | failed | HTTP 404 |
| PDT Partners | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Citadel | playwright | blocked | HTTP 403 |
| Point72 | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Hudson River Trading | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Jump Trading | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Ridgewater Capital | playwright | disabled | Placeholder: needs verified official URL |
| Quadrature Capital | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Optiver | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Two Sigma | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| D.E. Shaw | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Five Rings | playwright | failed | ConnectionError: HTTPSConnectionPool(host='www.fiveringscapital.com', port=443): Max retries exceeded with url: /careers (Caused by NameResolutionError("HTTPSConnection(host='www.fiveringscapital.com', port=443): Failed to resolve 'www.fiveringscapital.com' ([Errno 11001] getaddrinfo failed)")) |
| Voleon | playwright | failed | HTTP 404 |
| XTX Markets | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Susquehanna (SIG) | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| IMC Trading | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| DRW | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Virtu Financial | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Maven Securities | playwright | failed | HTTP 404 |
| Millennium | playwright | failed | ConnectTimeout: HTTPSConnectionPool(host='www.millennium.com', port=443): Max retries exceeded with url: /careers (Caused by ConnectTimeoutError(<HTTPSConnection(host='www.millennium.com', port=443) at 0x259ab416ba0>, 'Connection to www.millennium.com timed out. (connect timeout=8)')) |
| AQR Capital | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| G-Research | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| WorldQuant | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Squarepoint Capital | playwright | failed | HTTP 404 |
| Akuna Capital | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Flow Traders | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Anthropic | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| OpenAI | ashby | api_responding | Schema checked; confirm official ownership and run full collection |
| Netflix | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Roblox | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Duolingo | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Block (Square) | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Tesla | playwright | blocked | HTTP 403 |
| DoorDash | playwright | blocked | HTTP 403 |
| Asana | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Datadog | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Snap | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Ramp | ashby | api_responding | Schema checked; confirm official ownership and run full collection |
| Spotify | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Dropbox | playwright | failed | HTTP 404 |
| Pinterest | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Plaid | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Figma | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Discord | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Robinhood | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| C3.ai | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Blackstone | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| eBay | playwright | failed | SSLError: HTTPSConnectionPool(host='ebaycareers.com', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, "[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'ebaycareers.com'. (_ssl.c:1010)"))) |
| xAI | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| GitHub | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Palantir | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Lyft | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Twitch | playwright | failed | HTTP 404 |
| Capital One | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Intel | playwright | blocked | HTTP 403 |
| Wells Fargo | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Bank of America | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Boeing | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Booz Allen Hamilton | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Arrow Electronics | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| SLB | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Koch Industries | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Autodesk | playwright | blocked | HTTP 403 |
| TrueFirms | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Carousel (unconfirmed) | playwright | disabled | Placeholder: needs verified official URL |
| Emergent (unconfirmed) | playwright | disabled | Placeholder: needs verified official URL |
| Emerson | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| AlgoTest | playwright | failed | HTTP 404 |
| Brocolli (unconfirmed) | playwright | disabled | Placeholder: needs verified official URL |
| Matiks | playwright | disabled | Placeholder: needs verified official URL |
| Trellix | playwright | failed | ConnectionError: HTTPSConnectionPool(host='www.trellix.com', port=443): Max retries exceeded with url: /about/careers/ (Caused by ReadTimeoutError("HTTPSConnectionPool(host='www.trellix.com', port=443): Read timed out. (read timeout=15)")) |
| Lowe's India | playwright | failed | HTTP 404 |
| Wingify | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Layer Up (unconfirmed) | playwright | disabled | Placeholder: needs verified official URL |
| Nike | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Honeywell | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Redrob | playwright | blocked | HTTP 403 |
| Milestone (unconfirmed) | playwright | disabled | Placeholder: needs verified official URL |
| Redis | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Red Hat | playwright | reachable_unverified | HTTP only; extraction and pagination not verified |
| Perplexity | ashby | api_responding | Schema checked; confirm official ownership and run full collection |
| Linear | ashby | api_responding | Schema checked; confirm official ownership and run full collection |
| Vercel | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Glean | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |
| Graviton Research Capital | greenhouse | api_responding | Schema checked; confirm official ownership and run full collection |

