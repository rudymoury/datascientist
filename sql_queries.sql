-- SQLite
-- 1 . What was the total revenue to the nearest dollar for customers who have paid by credit card?
select round(sum(revenue))
from customers
where cc_payments > 0;

-- 2. What percentage of customers who have purchased female items have paid by credit card?
select 100 * sum(cc_payments)/sum(cc_payments + paypal_payments + afterpay_payments + apple_payments)
from customers
where female_items > 0
;

-- 3. What was the average revenue for customers who used either iOS, Android or Desktop?
select round(avg(revenue),2)
from customers
where ios_orders > 0
or android_orders > 0
or desktop_orders > 0
;

-- 4. We want to run an email campaign promoting a new mens luxury brand. Can you provide a list of customers we should send to?
select customer_id
from customers
-- 	Number of Men Apparel items purchased > 0
where mapp_items > 0