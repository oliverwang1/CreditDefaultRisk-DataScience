update previous_application set amt_annuity = 0 where amt_annuity = ''
update previous_application set amt_application = 0 where amt_application = ''


update app 
set total_prev_apps = q.total_prev_apps,
average_prev_app = q.average_prev_app,
avg_prev_annuity = q.avg_prev_annuity,
days_since_last_decision = q.days_since_last_decision,
reject_reason = q.reject_reason
from application_train app inner join 
(select count(*) as total_prev_apps, 
	avg(convert(decimal(9,2),amt_application)) as average_prev_app, 
	avg(convert(decimal(9,2),amt_annuity)) as avg_prev_annuity, 
	sk_id_curr,
	(SELECT top 1 days_Decision from previous_application p2 where p2.sk_id_curr = p1.sk_id_curr order by sk_id_prev desc) as days_since_last_decision,
	(SELECT top 1 code_reject_reason from previous_application p2 where p2.sk_id_curr = p1.sk_id_curr order by sk_id_prev desc) as reject_reason
from previous_application p1
group by sk_id_curr) q 
on app.SK_ID_CURR = q.sk_id_curr
