# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('catax', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportedOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Order Title - typically an email address', max_length=50)),
                ('email', models.CharField(help_text=b'email address for the order - usually matches title', max_length=50)),
                ('shiptype', models.CharField(help_text=b'Shipping type - US or Intl', max_length=10)),
                ('shipname', models.CharField(help_text=b'Shipping name', max_length=80)),
                ('shiporg', models.CharField(help_text=b'Shipping organization', max_length=80, blank=True)),
                ('shipaddr1', models.CharField(help_text=b'Shipping address - line 1', max_length=80)),
                ('shipaddr2', models.CharField(help_text=b'Shipping address - line 2', max_length=60, blank=True)),
                ('shipcity', models.CharField(help_text=b'Shipping city', max_length=40)),
                ('shipstate', models.CharField(help_text=b'Shipping state', max_length=2, blank=True)),
                ('shipzip', models.CharField(help_text=b'Shipping zip or postal code', max_length=10, blank=True)),
                ('shipcountry', models.CharField(help_text=b'Shipping country', max_length=40, blank=True)),
                ('shipregn', models.CharField(help_text=b'Shipping region, province, area, etc', max_length=30, blank=True)),
                ('shipphone', models.CharField(help_text=b'Shipping phone #', max_length=20, blank=True)),
                ('shipper', models.CharField(blank=True, help_text=b'Shipper / shipping carrier name', max_length=15, choices=[(b'Any', b'No Preference'), (b'UPS', b'UPS'), (b'FedEx', b'FedEx'), (b'DHL', b'DHL'), (b'Aero', b'Aero Logistics'), (b'Airborne', b'Airborne'), (b'USPS', b'US Postal Service (International only)'), (b'BAX', b'BAX Global'), (b'None', b'None (Will Call)'), (b'Other', b'Other (enter in "Special Instructions" field)')])),
                ('shipmethod', models.CharField(help_text=b'Shipping method', max_length=10, choices=[(b'ground', b'Ground'), (b'3day', b'3-day'), (b'2day', b'2-day'), (b'1day', b'Next Day'), (b'1dayAM', b'Next Day AM'), (b'IntlEcon', b'International Economy (5-7 days)'), (b'IntlExpr', b'International Express (2-3 days)'), (b'freight', b'Freight'), (b'willcall', b'Will Call')])),
                ('shiprate', models.CharField(help_text=b'Shipping multiplier of base (ground) rate', max_length=10, blank=True)),
                ('shipcost', models.FloatField(help_text=b'Shipping cost')),
                ('shippay', models.CharField(help_text=b"Shipping payment method - included, or billed to customer's card or account", max_length=10, choices=[(b'included', b'Included - Shipping paid with order'), (b'customer', b'Customer - Bill customer/3rd-party')])),
                ('shipprice', models.CharField(help_text=b'Shipping price', max_length=10, blank=True)),
                ('shipacct', models.CharField(help_text=b"Shipping account number, for shipping billed to customer's account", max_length=20, blank=True)),
                ('shipincl', models.CharField(help_text=b'Shipping included (not used much)', max_length=10, blank=True)),
                ('billtype', models.CharField(help_text=b'Billing type - US or Intl', max_length=10, blank=True)),
                ('billname', models.CharField(help_text=b'Billing name', max_length=80, blank=True)),
                ('billorg', models.CharField(help_text=b'Billing organization', max_length=80, blank=True)),
                ('billaddr1', models.CharField(help_text=b'Billing address - line 1', max_length=80, blank=True)),
                ('billaddr2', models.CharField(help_text=b'Billing address - line 2', max_length=60, blank=True)),
                ('billcity', models.CharField(help_text=b'Billing city', max_length=40, blank=True)),
                ('billstate', models.CharField(help_text=b'Billing state', max_length=2, blank=True)),
                ('billzip', models.CharField(help_text=b'Billing zip or postal code', max_length=10, blank=True)),
                ('billcountry', models.CharField(help_text=b'Billing country', max_length=20, blank=True)),
                ('billregn', models.CharField(help_text=b'Billing region, province, area, etc', max_length=30, blank=True)),
                ('billphone', models.CharField(help_text=b'Billing phone #', max_length=20, blank=True)),
                ('billfax', models.CharField(help_text=b'Billing fax #', max_length=20, blank=True)),
                ('billinitials', models.CharField(help_text=b'Billing employee initials', max_length=10, blank=True)),
                ('billemail', models.CharField(help_text=b'Billing email address for the order, if different than main order email', max_length=50, blank=True)),
                ('billsame', models.CharField(help_text=b'Billing address same as shipping address', max_length=3)),
                ('iagree', models.CharField(help_text=b'User has checked the "I Agree" box for the terms and conditions', max_length=3)),
                ('reftyp', models.CharField(help_text=b'Referral type for this order', max_length=10, choices=[(b'', b'Please Select'), (b'google', b'Google search'), (b'googlead', b'Google Ad'), (b'yahoo', b'Yahoo'), (b'search', b'Other search engine (please enter below)'), (b'dir', b'Web Directory (dmoz, Yahoo dir, etc - enter below)'), (b'press', b'Press release'), (b'repeat', b'Repeat business'), (b'referral', b'Referral or word-of-mouth (please enter below)'), (b'flyer', b'Brochure or flyer (please enter promo code below)'), (b'conf', b'Conference or Trade Show (please enter below)'), (b'list', b'Mailing list or newsgroup (please enter below)'), (b'project', b'Open-Source site (OpenBSD, Zope, etc - enter below)'), (b'mag', b'Magazine article (please enter mag and month/yr below)'), (b'magad', b'Magazine ad (please enter mag and month/yr below)'), (b'blog', b'Link from portal or blog (please enter below)'), (b'website', b'Other link or website (please enter below)'), (b'auction', b'Auction site (eBay, UBid, etc - please enter below)'), (b'other', b'Other - please enter below')])),
                ('refsrc', models.CharField(help_text=b'Referral source for "other" referral types', max_length=100, blank=True)),
                ('refnum', models.CharField(help_text=b'Purchase Order or customer reference number', max_length=30, blank=True)),
                ('approved_date', models.DateTimeField(help_text=b'Date order was approved (not used much)', null=True, blank=True)),
                ('saleinitials', models.CharField(help_text=b'Sales employee initials', max_length=10, blank=True)),
                ('paymeth', models.CharField(help_text=b'Payment method', max_length=12, choices=[(b'', b'Please Select'), (b'byccard', b'Credit Card'), (b'bycheck', b'Check in Advance'), (b'bypo', b'Purchase Order'), (b'bywire', b'Wire Transfer')])),
                ('payterms', models.CharField(blank=True, help_text=b'Payment terms', max_length=20, choices=[(b'ccard', b'card ending in'), (b'cod', b"COD Cashier's check"), (b'check', b'Company check (on approval)'), (b'internal', b'Internal use'), (b'net0', b'Net 0'), (b'net5', b'Net 5'), (b'net10', b'Net 10'), (b'net30', b'Net 30'), (b'po', b'Purchase Order (requires approval)'), (b'wire', b'Wire Transfer')])),
                ('payinitials', models.CharField(help_text=b'Payment employee initials', max_length=10, blank=True)),
                ('cclast4', models.CharField(help_text=b'Credit card - last 4 digits', max_length=10, blank=True)),
                ('ccmonth', models.IntegerField(help_text=b'Credit card expiry date - Month', null=True, blank=True)),
                ('ccyear', models.IntegerField(help_text=b'Credit card expiry date - Year', null=True, blank=True)),
                ('ccauthnum', models.IntegerField(help_text=b'Credit card authorization - confirmation number', null=True, blank=True)),
                ('cc_cvv', models.CharField(help_text=b'Credit card - CVV verification code', max_length=20, blank=True)),
                ('cc_corp_pin', models.IntegerField(help_text=b'Credit card - corporate PIN number', null=True, blank=True)),
                ('cc_charged_date', models.DateTimeField(help_text=b'Credit card - Date card was charged (only used in mid-2000s)', null=True, blank=True)),
                ('cc_initials', models.CharField(help_text=b'Credit card employee initials', max_length=10, blank=True)),
                ('taxcounty', models.CharField(help_text=b'Tax county', max_length=50, blank=True)),
                ('taxrate', models.CharField(help_text=b'Tax rate', max_length=10, blank=True)),
                ('salestax', models.CharField(help_text=b'Tax amount (exception - not used much)', max_length=10, blank=True)),
                ('orderdate', models.DateTimeField(help_text=b'Order date', null=True, blank=True)),
                ('orderstatus', models.CharField(help_text=b'Order status', max_length=15, choices=[(b'new', b'New'), (b'verified', b'Verified'), (b'canceled', b'Canceled'), (b'fraud', b'Fraud'), (b'invalid', b'Invalid'), (b'test', b'Test'), (b'open', b'Open'), (b'inprogress', b'In Progress'), (b'shipped', b'Shipped'), (b'paid', b'Paid'), (b'shippedandpaid', b'Shipped and Paid'), (b'returned', b'Returned'), (b'repair', b'In for repair'), (b'closed', b'Closed')])),
                ('ordernum', models.IntegerField(help_text=b'Order number - should match id')),
                ('instr', models.TextField(help_text=b'Special instructions for this order', blank=True)),
                ('internalnotes', models.TextField(help_text=b'Internal notes for this order', blank=True)),
                ('oldnotes', models.TextField(help_text=b'Old notes for this order (not used much)', blank=True)),
                ('adjustments', models.TextField(help_text=b'Adjustments, if any, to this order', blank=True)),
                ('adjustamt', models.CharField(help_text=b'Adjustment amount', max_length=10, blank=True)),
                ('costofgoods', models.CharField(help_text=b'Cost of Goods for this order, total', max_length=10, blank=True)),
                ('tracknumbers', models.TextField(help_text=b'Tracking numbers for this order', blank=True)),
                ('shipdate', models.DateTimeField(help_text=b'Shipping - Date shipped', null=True, blank=True)),
                ('shipinitials', models.CharField(help_text=b'Shipping employee initials', max_length=10, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImportedOrderLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('line', models.IntegerField(help_text=b'Order line item number - matches id')),
                ('title', models.CharField(help_text=b'Title - typically the same as Sku', max_length=50)),
                ('sku', models.CharField(help_text=b'Sku - typically the same as Title', max_length=50)),
                ('product', models.CharField(help_text=b'Product name - eRacks/<Sku>', max_length=50)),
                ('summary', models.TextField(help_text=b'Summary for this line item - changed items', blank=True)),
                ('qty', models.IntegerField(help_text=b'Quantity of this line item')),
                ('baseprice', models.FloatField(help_text=b'Base price of system')),
                ('totprice', models.FloatField(help_text=b'Total price of system')),
                ('notes', models.TextField(help_text=b'Notes for this line item', blank=True)),
                ('weight', models.IntegerField(help_text=b'Weight of this system', blank=True)),
                ('shipper', models.CharField(help_text=b'Name of shipper for this line item', max_length=50, blank=True)),
                ('shipdate', models.DateTimeField(help_text=b'Shipping - Date shipped', null=True, blank=True)),
                ('shipprice', models.FloatField(help_text=b'Shipping price of this system / line item', null=True, blank=True)),
                ('tracknum', models.CharField(help_text=b'Tracking number for this line item', max_length=50, blank=True)),
                ('serial', models.CharField(help_text=b'Serial number for this line item (Typically the Mac address)', max_length=50, blank=True)),
                ('serials', models.TextField(help_text=b'Multiple Serial numbers for this line item (Typically the Mac address)', blank=True)),
                ('details', models.TextField(help_text=b'Detailed / full config dictionary for this system', blank=True)),
                ('order', models.ForeignKey(help_text=b'Parent Order number', to='orders.ImportedOrder')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference_number', models.CharField(help_text=b'Customer Reference Number / Purchase Order Number', max_length=50, blank=True)),
                ('shipping', models.DecimalField(default=0, help_text=b'Shipping amount', max_digits=10, decimal_places=2)),
                ('shipping_method', models.CharField(default=b'ground', help_text=b'Choose preferred shipping method & speed', max_length=50, choices=[(b'ground', b'Ground'), (b'3day', b'3-day'), (b'2day', b'2-day'), (b'1day', b'Next Day'), (b'1dayAM', b'Next Day AM'), (b'IntlEcon', b'International Economy (5-7 days)'), (b'IntlExpr', b'International Express (2-3 days)'), (b'freight', b'Freight'), (b'willcall', b'Will Call')])),
                ('preferred_shipper', models.CharField(default=b'Any', help_text=b'Choose your preferred shipper', max_length=50, choices=[(b'Any', b'No Preference'), (b'UPS', b'UPS'), (b'FedEx', b'FedEx'), (b'DHL', b'DHL'), (b'Aero', b'Aero Logistics'), (b'Airborne', b'Airborne'), (b'USPS', b'US Postal Service (International only)'), (b'BAX', b'BAX Global'), (b'None', b'None (Will Call)'), (b'Other', b'Other (enter in "Special Instructions" field)')])),
                ('shipping_payment', models.CharField(default=b'included', help_text=b'Choose shipping payment method (Put account number & details in "Special Instructions" below as needed)', max_length=80, choices=[(b'included', b'Included - Shipping paid with order'), (b'customer', b'Customer - Bill customer/3rd-party')])),
                ('referral_type', models.CharField(default=b'Please Select', help_text=b'How did you hear of us?', max_length=80, choices=[(b'', b'Please Select'), (b'google', b'Google search'), (b'googlead', b'Google Ad'), (b'yahoo', b'Yahoo'), (b'search', b'Other search engine (please enter below)'), (b'dir', b'Web Directory (dmoz, Yahoo dir, etc - enter below)'), (b'press', b'Press release'), (b'repeat', b'Repeat business'), (b'referral', b'Referral or word-of-mouth (please enter below)'), (b'flyer', b'Brochure or flyer (please enter promo code below)'), (b'conf', b'Conference or Trade Show (please enter below)'), (b'list', b'Mailing list or newsgroup (please enter below)'), (b'project', b'Open-Source site (OpenBSD, Zope, etc - enter below)'), (b'mag', b'Magazine article (please enter mag and month/yr below)'), (b'magad', b'Magazine ad (please enter mag and month/yr below)'), (b'blog', b'Link from portal or blog (please enter below)'), (b'website', b'Other link or website (please enter below)'), (b'auction', b'Auction site (eBay, UBid, etc - please enter below)'), (b'other', b'Other - please enter below')])),
                ('referral_source', models.CharField(help_text=b'Please specify if Referral Type is "Other"', max_length=80, blank=True)),
                ('special_instructions', models.TextField(help_text=b'Customer special instructions for this order - shipping, build, options, etc', blank=True)),
                ('cart', models.TextField(help_text=b'Serialized copy of shopping cart at time of purchase', blank=True)),
                ('agree_to_terms', models.BooleanField(help_text=b'Customer agreed to terms and accepted EULA')),
                ('comment', models.TextField(help_text=b'Internal comments on this order', blank=True)),
                ('status', models.CharField(help_text=b'Order status', max_length=50, choices=[(b'new', b'New'), (b'verified', b'Verified'), (b'canceled', b'Canceled'), (b'fraud', b'Fraud'), (b'invalid', b'Invalid'), (b'test', b'Test'), (b'open', b'Open'), (b'inprogress', b'In Progress'), (b'shipped', b'Shipped'), (b'paid', b'Paid'), (b'shippedandpaid', b'Shipped and Paid'), (b'returned', b'Returned'), (b'repair', b'In for repair'), (b'closed', b'Closed')])),
                ('source', models.CharField(default=b'website', help_text=b'Source of order - Website, Imported Zope order, Phone, etc', max_length=50, choices=[(b'zope', b'Legacy Zope Order'), (b'website', b'Website order'), (b'other', b'Other - see comments')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('processed', models.DateTimeField(null=True, blank=True)),
                ('bill_to_address', models.ForeignKey(related_name='order_bill_to', to='customers.Address', help_text=b'Bill to this address')),
                ('california_tax', models.ForeignKey(blank=True, to='catax.Catax', help_text=b'California shipments please choose county/city', null=True, verbose_name=b'Sales Tax (CA Only)')),
                ('customer', models.ForeignKey(related_name='orders', to='customers.Customer')),
                ('ship_to_address', models.ForeignKey(related_name='order_ship_to', to='customers.Address', help_text=b'Ship to this address')),
            ],
            options={
                'db_table': 'orders',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payment_method', models.CharField(default=b'Please Select', help_text=b'Payment method', max_length=12, choices=[(b'', b'Please Select'), (b'byccard', b'Credit Card'), (b'bycheck', b'Check in Advance'), (b'bypo', b'Purchase Order'), (b'bywire', b'Wire Transfer')])),
                ('payment_terms', models.CharField(blank=True, help_text=b'Payment terms', max_length=20, choices=[(b'ccard', b'card ending in'), (b'cod', b"COD Cashier's check"), (b'check', b'Company check (on approval)'), (b'internal', b'Internal use'), (b'net0', b'Net 0'), (b'net5', b'Net 5'), (b'net10', b'Net 10'), (b'net30', b'Net 30'), (b'po', b'Purchase Order (requires approval)'), (b'wire', b'Wire Transfer')])),
                ('last_4', models.CharField(help_text=b'Credit card - last 4 digits', max_length=10, blank=True)),
                ('expiry_date', models.DateField(help_text=b'Credit card expiry date - MMYY', null=True, blank=True)),
                ('auth_num', models.IntegerField(help_text=b'Credit card authorization - confirmation number', null=True, blank=True)),
                ('comments', models.TextField(help_text=b'Comments on this payment', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(help_text=b'Order number', to='orders.Order')),
                ('user', models.ForeignKey(help_text=b'Customer username or employee processing payment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]