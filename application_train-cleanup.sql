select top 10000 * from [train_v4_clean_polynomial_domain]

update [train_v4_clean_polynomial_domain] set average_prev_app = 0 where average_prev_app IS NULL
update [train_v4_clean_polynomial_domain] set avg_prev_annuity = 0 where avg_prev_annuity IS NULL
update [train_v4_clean_polynomial_domain] set days_since_last_decision = 0 where days_since_last_decision IS NULL
update [train_v4_clean_polynomial_domain] set reject_reason = 0 where reject_reason IS NULL
update [train_v4_clean_polynomial_domain] set avg_credit_usage = 0 where avg_credit_usage IS NULL
update [train_v4_clean_polynomial_domain] set total_underpayments = 0 where total_underpayments IS NULL
update [train_v4_clean_polynomial_domain] set total_payments = 0 where total_payments IS NULL
update [train_v4_clean_polynomial_domain] set months_balance = 0 where months_balance IS NULL
update [train_v4_clean_polynomial_domain] set avg_payment_compared_to_minimum = 0 where avg_payment_compared_to_minimum IS NULL
update [train_v4_clean_polynomial_domain] set total_prev_apps = 0 where total_prev_apps IS NULL