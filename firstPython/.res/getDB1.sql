------根据用户提供的list，找到对应的支付商数据，并备份
create table bak_arm_payment_dg20191118 as
select * from arm_payment p where exists (
select * from bak_arm_payment_dg_input t where t.pay_type in ('THT1118') and t.bill_no=p.bill_no   --and t.pay_amt=p.pay_amt
) and p.match_order_flag='N' and p.manual_confirm is null ;
----根据备份表，对相应的支付商打标DB。其中与errorrefund匹配成Y的数据，不打DB
select * from arm_payment p where exists (
select * from bak_arm_payment_dg20191106 t where t.id=p.id )
and p.match_order_flag<>'Y';
---update,共108条
update arm_payment p 
set p.reason_code='DB',p.action_code='AN',p.manual_confirm='Y',p.confirm_id='dugang@',p.confirm_date=sysdate
where exists (
select * from bak_arm_payment_dg_input t where t.pay_type in ('THT1118') and t.bill_no=p.bill_no   --and t.pay_amt=p.pay_amt
) and p.match_order_flag='N' and p.manual_confirm is null ;
-------------------------------
delete from  bak_arm_payment_dg_input t ;

select t.*,t.rowid from  bak_arm_payment_dg_input t where t.pay_type='THT1118' ;

update bak_arm_payment_dg_input t 
--set t.bill_no=trim(t.bill_no)
set t.bill_no=substr(t.bill_no,1,length(t.bill_no)-1)
where t.pay_type='THT1118'
