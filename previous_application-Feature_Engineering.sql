update previous_application set amt_annuity = 0 where amt_annuity = ''
update previous_application set amt_application = 0 where amt_application = ''

select count(*), 
	avg(convert(decimal(9,2),amt_application)) as average_prev_app, 
	avg(convert(decimal(9,2),amt_annuity)) as avg_prev_annuity, 
	sk_id_curr 
from previous_application 
group by sk_id_curr

select * from previous_application