select * from [train_v4_clean_polynomial_domain]
select count(distinct SK_ID_CURR) from credit_card_balance


update app set AVG_CREDIT_USAGE = q.AVG_CREDIT_USAGE
from [train_v4_clean_polynomial_domain] app inner join (
select AVG(
convert(decimal(9,2),AMT_BALANCE)/convert(decimal(9,2),AMT_CREDIT_LIMIT_ACTUAL) ) as AVG_CREDIT_USAGE, SK_ID_CURR
from credit_card_balance where convert(decimal(9,2),AMT_CREDIT_LIMIT_ACTUAL) > 0.0
group by SK_ID_CURR) as q on app.SK_ID_CURR = q.SK_ID_CURR

update credit_card_balance set AMT_PAYMENT_CURRENT = 0 where AMT_PAYMENT_CURRENT = ''
update credit_card_balance set AMT_INST_MIN_REGULARITY = 0 where AMT_INST_MIN_REGULARITY = ''

update app set AVG_PAYMENT_COMPARED_TO_MINIMUM = q.AVG_PAYMENT_COMPARED_TO_MINIMUM
from [train_v4_clean_polynomial_domain] app inner join (
select AVG(convert(decimal(9,2),ISNULL(AMT_PAYMENT_CURRENT,0.00))/convert(decimal(9,2),ISNULL(AMT_INST_MIN_REGULARITY,0.00))) as AVG_PAYMENT_COMPARED_TO_MINIMUM, SK_ID_CURR from credit_card_balance
where convert(decimal(9,2),ISNULL(AMT_INST_MIN_REGULARITY,0.00)) > 0
group by SK_ID_CURR) as q on app.SK_ID_CURR = q.SK_ID_CURR

update app set TOTAL_UNDERPAYMENTS = q.TOTAL_UNDERPAYMENTS 
from [train_v4_clean_polynomial_domain] app inner join (
select count(*) as TOTAL_UNDERPAYMENTS, SK_ID_CURR FROM credit_card_balance 
where convert(decimal(9,2),ISNULL(AMT_PAYMENT_CURRENT,0.00)) < convert(decimal(9,2),ISNULL(AMT_INST_MIN_REGULARITY,0.00))
group by SK_ID_CURR) as q on app.SK_ID_CURR = q.SK_ID_CURR

update app set TOTAL_PAYMENTS = q.TOTAL_PAYMENTS
from [train_v4_clean_polynomial_domain] app inner join (
select count(*) as TOTAL_PAYMENTS, SK_ID_CURR FROM credit_card_balance 
group by SK_ID_CURR) as q on app.SK_ID_CURR = q.SK_ID_CURR

update app set months_balance = q.months_balance
from [train_v4_clean_polynomial_domain] app inner join (
select min(convert(decimal(9,2),Months_balance)) as months_balance, sk_id_curr from credit_card_balance group by SK_ID_CURR)
as q on app.SK_ID_CURR = q.SK_ID_CURR