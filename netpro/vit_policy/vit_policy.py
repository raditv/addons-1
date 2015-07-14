# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the OpenERP plugin for Dia !
from openerp.osv import fields,osv
import time

class netpro_policy(osv.osv):
    _name = 'netpro.policy'
    _rec_name = 'policy_no'
    _columns = {
        'policy_no': fields.char('Policy No'),
        'reference_no': fields.char('Reference No'),
        'quotation_no': fields.char('Quotation No'),
        'ci': fields.char('C/I'),
        'corporate_id': fields.char('Corporate ID'),
        'policy_category': fields.many2one('netpro.policy_category','Policy Category'),
        'policy_type': fields.many2one('netpro.policy_type', 'Policy Type'),
        'branch_id': fields.many2one('res.partner', 'Branch'),
        'marketing_officer_id': fields.many2one('res.partner', 'Marketing Officer'),
        'policy_holder_id': fields.many2one('res.partner', 'Policy Holder'),
        'policy_group_id': fields.many2one('netpro.policy_group', 'Group'),
        'insurance_period_start': fields.date('Insurance Period Start'),
        'insurance_period_end': fields.date('Insurance Period End'),
        'exclusive_period': fields.boolean('Exclusive Period'),
        'toc_id': fields.many2one('netpro.toc', 'TOC'),
        'ujroh': fields.float('Ujroh'),
        'currency_id': fields.many2one('res.currency', 'Currency'),
        'policy_payor_id': fields.many2one('res.partner', 'Policy Payor'),
        'insurance_source_id': fields.many2one('res.partner', 'Insurance Source'),
        'segment_id': fields.many2one('netpro.segment', 'Segment'),
        'pic_id': fields.many2one('res.partner', 'PIC'),
        'policy_date': fields.date('Policy Date'),
        'business_source_id': fields.many2one('res.partner', 'Business Source'),
        'lob_id': fields.many2one('netpro.lob', 'LOB'),
        'occupation_id': fields.many2one('netpro.occupation', 'Occupation'),
        'existing_policy_no_id': fields.many2one('res.partner', 'Existing Policy No'),
        'province_id': fields.many2one('netpro.province', 'Region'),
        'remarks': fields.text('Remarks'),
        'payment_option_mode_id': fields.many2one('netpro.payment_option_mode', 'Payment Option Mode'),
        'payment_option_installment_id': fields.many2one('netpro.payment_option_installment', 'Payment Option Installment'),
        'refund_adj': fields.float('Refund Adj.'),
        'refund_with_claim_deduction': fields.boolean('Refund with Claim Deduction'),
        'endorsement_fee': fields.float('Endorsement Fee'),
        'endorsement_with_installment': fields.boolean('Endorsement with Installment'),
        'refund_type_id': fields.many2one('netpro.refund_type', 'Add / Refund Type'),
        'no_refund_changing_premium_difference': fields.boolean('No refund changing premium difference'),
        'print_card_name': fields.char('Print Name'),
        'print_card_order': fields.many2one('netpro.print_card_order', 'Print Order'),
        'print_card_birthdate': fields.boolean('Print Birthdate'),
        'print_card_sex': fields.boolean('Print Sex'),
        'print_card_plan': fields.boolean('Print Plan'),
        'tpa_id': fields.many2one('netpro.tpa', 'TPA'),
        'calculation_method_id': fields.many2one('netpro.calculation_method', 'Calculation Method'),
        'prorate_calc_method_id': fields.many2one('netpro.prorate_calc_method', 'Prorate Calc Method'),
        'expired_claim_receipt_id': fields.many2one('netpro.expired_claim_receipt', 'Expired Claim Receipt'),
        'payment_due_days': fields.integer('Payment Due Days'),
        'payment_due_interval_id': fields.many2one('netpro.payment_due_interval', 'Payment Due Interval'),
        'max_age_children': fields.integer('Max Age Children'),
        'max_children_id': fields.many2one('netpro.max_children', 'Max Children'),
        'max_children_maternity_id': fields.many2one('netpro.max_children_maternity', 'Max Children Maternity'),
        'card_type_id': fields.many2one('netpro.card_type', 'Card Type'),
        'pre_existing_condition_id': fields.many2one('netpro.pre_existing_condition', 'Pre Existing Condition'),
        'tolerance_up_room_percent': fields.integer('Tolerance Up Room Percent'),
        'tolerance_up_room_amount': fields.float('ToleranceUpRoomAmount'),
        'up_room_class_id': fields.many2one('netpro.up_room_class', 'Up Room Class'),
        'up_room_class_days': fields.integer('Up Room Class Days'),
        'prorate_after_tolerance_addition': fields.boolean('Prorate After Tolerance Addition'),
        'allow_adult_child_premium': fields.boolean('Allow Adult Child Premium'),
        'have_sub_company': fields.boolean('Have Sub Company'),
        'female_spouse_only': fields.boolean('Female Spouse Only'),
        'profit_sharing': fields.boolean('Profit Sharing'),
        'use_in_house_clinic': fields.boolean('Use In House Clinic'),
        'allow_plan_sharing': fields.boolean('Allow Plan Sharing'),
        'renewal_with_old_card': fields.boolean('Renewal with Old Card'),
        'renewal_manual': fields.boolean('Renewal Manual (TPA)'),
        'commission_by_gross_premium': fields.boolean('Commission by Gross Premium'),
        'allow_excesson_reimbursement': fields.boolean('Allow Excess on Reimbursement'),
        'aso_deposit': fields.float('ASO Deposit'),
        'bank_id': fields.many2one('res.partner.bank', 'Bank'),
        'vaccount_no': fields.char('V Account No'),
        'bank_optional_id': fields.many2one('res.partner.bank', 'Bank Optional', help='Relasi ke Partner Bank'),
        'vaccount_no_optional': fields.char('V Account No Optional'),
        'policy_status': fields.char('Policy Status'),
        'endorsement_date': fields.date('Endorsement Date'),
        'email_date': fields.date('EmailDate'),
        'int_endorsement_no': fields.integer('Int. Endorsement No'),
        'ext_endorsement_no': fields.integer('Ext. Endorsement No'),
        'pno': fields.integer('PNO'),
        'ppno': fields.integer('PPNO'),
        'cancel_policy': fields.boolean('Cancel Policy'),
        'profit_sharing_endorsement': fields.boolean('Profit Sharing Endorsement'),
        'created_by_id': fields.many2one('res.partner', 'Created By'),
        'created_by_date': fields.datetime('Created By Date'),
        'last_edited_by_id': fields.many2one('res.partner', 'Last Edited By'),
        'last_edited_by_date': fields.datetime('Last Edited By Date'),
        'approved_by_id': fields.many2one('res.partner', 'Approved By'),
        'approved_by_date': fields.datetime('Approved By Date'),
        'claim_rule_reimbursement_payee_id': fields.many2one('netpro.claim_rule', 'Reimbursement Payee'),
        'claim_rule_excess_payor_id': fields.many2one('netpro.claim_rule', 'Excess Payor'),
        'claim_rule_refund_payee_id': fields.many2one('netpro.claim_rule', 'Refund Payee'),
        'correspondence_rule_premium_id': fields.many2one('netpro.correspondence_rule', 'Premium'),
        'correspondence_rule_claim_id': fields.many2one('netpro.correspondence_rule', 'Claim'),
        'discount_special_discount': fields.float('Special Discount'),
        'discount_direct_discount': fields.float('Direct Discount'),
        'discount_discount_amount': fields.float('Discount Amount'),
        'discount_discount_only_apply_on_policy': fields.boolean('Discount Only Apply On Policy'),
        'loading_cc_loading': fields.float('CC Loading'),
        'deposit_deposit_recovery': fields.float('Deposit Recovery'),
        'claim_reimbursement_transfer_fee': fields.float('Fee (per employee)'),
        'other_settings_admin_cost': fields.float('Admin Cost'),
        'other_settings_card_fee': fields.float('@Card Fee'),
        'other_settings_total_card_fee': fields.float('Total Card Fee'),
        'other_settings_total_cdmin_cost': fields.float('Total Admin Cost'),
        'other_settings_stamp_duty': fields.float('Stamp Duty'),
        'other_settings_interest': fields.float('Interest'),
        'pool_fund_info_pool_fund': fields.float('Pool Fund'),
        'pool_fund_info_max_pool_fund_member': fields.integer('Max Pool Fund Member'),
        'pool_fund_info_max_member_pool_fund': fields.float('@Max Member Pool Fund'),
        'pool_fund_info_remarks': fields.text('Remarks'),
        'edc_apply_prorate': fields.boolean('Apply Prorate'),
        'edc_show_excess_amount': fields.boolean('Show Excess Amount'),
        'edc_show_excess_remarks': fields.boolean('Show Excess Remarks'),
        'edc_excess_remarks': fields.text('Excess Remarks'),
        'edc_disable_edc_for_inpatient': fields.boolean('Disable EDC For Inpatient'),
        'edc_disable_edc_for_outpatient': fields.boolean('Disable EDC For Outpatient'),
        'edc_disable_edc_for_maternity': fields.boolean('Disable EDC For Maternity'),
        'edc_disable_edc_for_dental': fields.boolean('Disable EDC For Dental'),
        'edc_disable_swipe_for_excessed_limit': fields.boolean('Disable Swipe For Excessed Limit'),
        'edc_ignore_claim_over_below_settings': fields.boolean('Ignore Claim Over Below Settings'),
        'edc_inpatient': fields.integer('Inpatient'),
        'edc_outpatient': fields.integer('Outpatient'),
        'edc_maternity': fields.integer('Maternity'),
        'edc_dental': fields.integer('Dental'),
        'profit_sharing_sharing_remarks': fields.text('Sharing Remarks'),
        'profit_sharing_gross_premium': fields.float('Gross Premium'),
        'profit_sharing_claim_paid': fields.float('Claim Paid'),
        'profit_sharing_claim_ratio': fields.float('Claim Ratio'),
        'profit_sharing_formula': fields.text('Formula'),
        'profit_sharing_profit_sharing': fields.float('Profit Sharing'),
        'profit_sharing_adjustment': fields.float('Adjustment'),
        'profit_sharing_profit_sharing_amt': fields.float('Profit Sharing Amt'),
        'coverage_ids': fields.one2many('netpro.coverage', 'policy_id', 'Coverages', ondelete='cascade'),
        'class_ids': fields.one2many('netpro.class', 'policy_id', 'Classes', ondelete='cascade'),
        'plan_schedule_ids': fields.one2many('netpro.plan_schedule', 'policy_id', 'Plan Schedules', ondelete='cascade'),
        'business_source_ids': fields.one2many('netpro.business_source', 'policy_id', 'Business Sources', ondelete='cascade'),
        'ci_date': fields.date('C/I Date'),
    }
    _defaults = {
        'ci_date' : lambda*a : time.strftime("%Y-%m-%d")
    }
    def create(self, cr, uid, vals, context=None):
        nomor = self.pool.get('ir.sequence').get(cr, uid, 'policy_seq') or '/'
        vals.update({
            'policy_no':nomor,
        })
        new_id = super(netpro_policy, self).create(cr, uid, vals, context=context)
        return new_id
netpro_policy()

class netpro_branch(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _columns = {
        'start_date'                : fields.date('Start Date'),
        'end_date'                  : fields.date('End Date'),
        'last_close_month'          : fields.integer('Last Close Month'),
        'last_close_year'           : fields.integer('Last Close Year'),
        'last_consolidated_month'   : fields.integer('Last Consolidated Year'),
        'last_consolidated_year'    : fields.integer('Last Consolidated Year'),
        'production_locked_date'    : fields.date('Production Locked Date'),
        'finance_locked_date'       : fields.date('Finance Locked Date'),
        'backdated_date'            : fields.date('Backdated Date'),
        'backdated_date'            : fields.date('Backdated Date'),
        'kpp_id'                    : fields.many2one('netpro.kpp', 'KPP'),
        'profit_loss_account'       : fields.many2one('account.account', 'Profit / Loss Account'),
        'tax_account'               : fields.many2one('account.account', 'Tax Account'),
        'dividen_account'           : fields.many2one('account.account', 'Dividen Account'),
        'inter_office_account'      : fields.many2one('account.account', 'Inter-Office Account'),
        'gain_loss_account'         : fields.many2one('account.account', 'Gain / Loss Account'),
        'retained_earnings'         : fields.many2one('account.account', 'Retained Earnings'),
        'active'                    : fields.boolean('Active'),
        'operating_branch'          : fields.boolean('Operating Branch'),
        'syariah_branch'            : fields.boolean('Syariah Branch'),
    }
netpro_branch()

class netpro_kpp(osv.osv):
    _name = 'netpro.kpp'
    _columns = {
        'kpp_id': fields.char('KPP ID'),
        'name': fields.char('Name'),
    }

class netpro_tpa(osv.osv):
    _name = 'netpro.tpa'
    _columns = {
        'name': fields.char('Name'),
        'code': fields.char('Code'),
    }
netpro_tpa()

class netpro_policy_category(osv.osv):
    _name = 'netpro.policy_category'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_policy_category()

class netpro_policy_type(osv.osv):
    _name = 'netpro.policy_type'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_policy_type()

class netpro_policy_group(osv.osv):
    _name = 'netpro.policy_group'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_policy_group()

class netpro_toc(osv.osv):
    _name = 'netpro.toc'
    _columns = {
        'name': fields.char('TOC'),
        'description': fields.text('Description'),
        'ujroh': fields.float('Ujroh'),
    }
netpro_toc()

class netpro_segment(osv.osv):
    _name = 'netpro.segment'
    _columns = {
        'name': fields.char('Segment'),
        'description': fields.text('Description'),
    }
netpro_segment()

# pindah ke vit_actuary
# class netpro_lob(osv.osv):
#     _name = 'netpro.lob'
#     _columns = {
#         'name': fields.char('LOB'),
#         'description': fields.text('Description'),
#     }
# netpro_lob()

class netpro_occupation(osv.osv):
    _name = 'netpro.occupation'
    _columns = {
        'name': fields.char('Occupation'),
        'description': fields.text('Description'),
    }
netpro_occupation()

class netpro_province(osv.osv):
    _name = 'netpro.province'
    _columns = {
        'name': fields.char('Name'),
        'country_id': fields.many2one('res.country', 'Country'),
    }
netpro_province()

class netpro_payment_option_mode(osv.osv):
    _name = 'netpro.payment_option_mode'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_payment_option_mode()

class netpro_payment_option_installment(osv.osv):
    _name = 'netpro.payment_option_installment'
    _columns = {
        'name': fields.char('Name'),
        'point': fields.integer('Point'),
        'description': fields.text('Description'),
    }
netpro_payment_option_installment()

class netpro_refund_type(osv.osv):
    _name = 'netpro.refund_type'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_refund_type()

class netpro_print_card_order(osv.osv):
    _name = 'netpro.print_card_order'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_print_card_order()

class netpro_calculation_method(osv.osv):
    _name = 'netpro.calculation_method'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_calculation_method()

class netpro_prorate_calc_method(osv.osv):
    _name = 'netpro.prorate_calc_method'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_prorate_calc_method()

class netpro_expired_claim_receipt(osv.osv):
    _name = 'netpro.expired_claim_receipt'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_expired_claim_receipt()

class netpro_payment_due_interval(osv.osv):
    _name = 'netpro.payment_due_interval'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_payment_due_interval()

class netpro_max_children(osv.osv):
    _name = 'netpro.max_children'
    _columns = {
        'name': fields.char('Name'),
        'point': fields.integer('Point'),
        'description': fields.text('Description'),
    }
netpro_max_children()

class netpro_max_children_maternity(osv.osv):
    _name = 'netpro.max_children_maternity'
    _columns = {
        'name': fields.char('Name'),
        'point': fields.integer('Point'),
        'description': fields.text('Description'),
    }
netpro_max_children_maternity()

class netpro_card_type(osv.osv):
    _name = 'netpro.card_type'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_card_type()

class netpro_pre_existing_condition(osv.osv):
    _name = 'netpro.pre_existing_condition'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_pre_existing_condition()

class netpro_up_room_class(osv.osv):
    _name = 'netpro.up_room_class'
    _columns = {
        'name': fields.char('Name'),
        'point': fields.integer('Point'),
    }
netpro_up_room_class()

class netpro_policy_status(osv.osv):
    _name = 'netpro.policy_status'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_policy_status()

class netpro_coverage(osv.osv):
    _name = 'netpro.coverage'
    _rec_name = 'no_plan'
    _columns = {
        'product_type_id': fields.many2one('netpro.product_type', 'Product Type'),
        'product_id': fields.many2one('netpro.product_id', 'Product ID'),
        'reimbursement': fields.float('Reimbursement'),
        'provider': fields.float('Provider'),
        'excess_pay_on_the_spot': fields.boolean('Excess Pay on the Spot'),
        'swipe_card': fields.boolean('Swipe Card'),
        'show_card': fields.boolean('ShowCard'),
        'reimbursement_boolean': fields.boolean('Reimbursement'),
        'no_plan': fields.integer('No Plan'),
        'no_of_benefit': fields.integer('No Of Benefit'),
        'default_limit_id': fields.many2one('netpro.default_limit', 'Default Limit'),
        'annual_limit_per_disability': fields.boolean('Annual Limit Per Disability'),
        'family_limit': fields.boolean('Family Limit'),
        'family_premium': fields.boolean('Family Premium'),
        'use_child_premium': fields.boolean('Use Child Premium'),
        'aso_coverage': fields.boolean('ASO Coverage'),
        'hi_plan': fields.boolean('Hi Plan'),
        'maximum_age_employee': fields.integer('Maximum Age Employee'),
        'maximum_age_spouse': fields.integer('Maximum Age Spouse'),
        'maximum_age_children': fields.integer('Maximum Age Children'),
        'aso_fee_per_member': fields.float('ASO Fee Per Member'),
        'aso_commission': fields.float('ASO Commission'),
        'aso_commission_in_percent': fields.float('ASO Commission In Percent'),
        'aso_fee_per_claim': fields.float('ASO Fee Per Claim'),
        'aso_fee_per_claim_amount': fields.float('ASO Fee Per Claim Amount'),
        'not_process_excesson_deposit': fields.boolean('Not Process Excess on Deposit'),
        'print_option_seq_no': fields.integer('Seq No.'),
        'print_option_print_text_on_card': fields.char('Print Text (On Card)'),
        'print_card_with_plan_amount': fields.boolean('Print Card with Plan Amount'),
        'membership_option_not_allowed_for_employee': fields.boolean('Not Allowed for Employee'),
        'membership_option_not_allowed_for_spouse': fields.boolean('Not Allowed for Spouse'),
        'membership_option_not_allowed_for_child': fields.boolean('Not Allowed for Child'),
        'policy_id': fields.many2one('netpro.policy', 'Policy'),
    }
netpro_coverage()

class netpro_class(osv.osv):
    _name = 'netpro.class'
    _rec_name = 'class_no'
    _columns = {
        'class_no': fields.integer('Class No'),
        'short_desc': fields.char('Short Desc'),
        'description': fields.text('Description'),
        'policy_id': fields.many2one('netpro.policy', 'Policy'),
        'membership_plan_employee_ids': fields.one2many('netpro.membership_plan_employee', 'class_id', 'Membership Plans Employee', ondelete='cascade'),
        'membership_plan_spouse_ids': fields.one2many('netpro.membership_plan_spouse', 'class_id', 'Membership Plans spouse_limit', ondelete='cascade'),
        'membership_plan_child_ids': fields.one2many('netpro.membership_plan_child', 'class_id', 'Membership Plans Child', ondelete='cascade'),
    }
netpro_class()

class netpro_plan_schedule(osv.osv):
    _name = 'netpro.plan_schedule'
    _rec_name = 'product_plan_base_id'
    _columns = {
        'product_plan_base_id': fields.many2one('netpro.product_plan_base', 'Product Plan'),
        'bamount': fields.float('BAmount'),
        'reimbursement': fields.float('Reimbursement'),
        'reimbursement_affect_to_benefit': fields.boolean('Reimbursement Affect To Benefit'),
        'individual_overall_limit_amount_point': fields.integer('Individual Overall Limit Amount'),
        'individual_overall_limit_amount_interval': fields.integer('Individual Overall Limit Amount Interval'),
        'family_overall_limit_amount_point': fields.integer('Family Overall Limit Amount'),
        'family_overall_limit_amount_interval': fields.integer('Family Overall Limit Amount Inteval'),
        'dependant_limit': fields.integer('Dependant Limit'),
        'spouse_limit': fields.integer('Spouse Limit'),
        'child_limit': fields.integer('@Child Limit'),
        '1_dependant': fields.char('+1 Dependant'),
        '2_dependant': fields.char('+2 Dependant'),
        '3_dependant': fields.char('+3 Dependant'),
        '4_dependant': fields.char('+4 Dependant'),
        '5_dependant': fields.char('+5 Dependant'),
        '6_dependant': fields.char('+6 Dependant'),
        '7_dependant': fields.char('+7 Dependant'),
        '8_dependant': fields.char('+8 Dependant'),
        '9_dependant': fields.char('+9 Dependant'),
        'aggregate_limit': fields.integer('Aggregate Limit'),
        'group_discount': fields.float('Group Discount'),
        'premium_discount': fields.float('Premium Discount'),
        'loading': fields.float('Loading'),
        'deductible': fields.float('Deductible'),
        'no_refund': fields.boolean('No Refund'),
        'no_refund_if_any_claim': fields.boolean('No Refund If Any Claim'),
        'hi_plan': fields.boolean('Hi Plan', help='Apply As Charge if R&B Same or Lower than Taken Benefit'),
        'aso_plan': fields.boolean('ASO Plan'),
        'maximum_age_employee': fields.integer('For Employee'),
        'maximum_age_spouse': fields.integer('For Spouse'),
        'maximum_age_children': fields.integer('For Children'),
        'sequence_no': fields.integer('Sequence No'),
        'provider_level_id': fields.many2one('netpro.provider_level', 'Provider Level'),
        'plan_schedule_detail_benefit_schedule_ids': fields.one2many('netpro.plan_schedule_detail_benefit_schedule', 'plan_schedule_id', 'Plan Schedule', ondelete='cascade'),
        'policy_id': fields.many2one('netpro.policy', 'Policy'),
    }
netpro_plan_schedule()

class netpro_business_source(osv.osv):
    _name = 'netpro.business_source'
    _rec_name = 'agent_id'
    _columns = {
        'agent_id': fields.many2one('netpro.agent', 'Agent'),
        'business_source_type_id': fields.many2one('netpro.business_source_type', 'Type'),
        'commission': fields.float('Commission'),
        'commission_only_apply_on_new_business': fields.boolean('Commission Only Apply On New Business'),
        'aso_commission': fields.boolean('ASO Commission'),
        'aso_commissiononly_apply_on_new_business': fields.boolean('ASO Commission only apply on New Business'),
        'aso_remarks_by_system': fields.text('ASO Remarks by System'),
        'policy_id': fields.many2one('netpro.policy', 'Policy'),
    }
netpro_business_source()

#>>> pindah ke actuary
# class netpro_product_type(osv.osv):
#     _name = 'netpro.product_type'
#     _columns = {
#         'name': fields.char('Product Type'),
#         'description': fields.text('Description'),
#     }
# netpro_product_type()

class netpro_product_id(osv.osv):
    _name = 'netpro.product_id'
    _columns = {
        'name': fields.char('Product ID'),
        'description': fields.text('Description'),
    }
netpro_product_id()

class netpro_default_limit(osv.osv):
    _name = 'netpro.default_limit'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_default_limit()

class netpro_product_plan_base(osv.osv):
    _name = 'netpro.product_plan_base'
    _columns = {
        'pplan': fields.char('PPlan'),
        'name': fields.char('Name'),
    }
netpro_product_plan_base()

class netpro_provider_level(osv.osv):
    _name = 'netpro.provider_level'
    _rec_name = 'plevel'
    _columns = {
        'plevel': fields.char('PLevel'),
        'description': fields.text('Description'),
    }
netpro_provider_level()

class netpro_agent(osv.osv):
    _name = 'netpro.agent'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_agent()

class netpro_business_source_type(osv.osv):
    _name = 'netpro.business_source_type'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_business_source_type()

class netpro_membership_plan_employee(osv.osv):
    _name = 'netpro.membership_plan_employee'
    _rec_name = 'class_id'
    _columns = {
        'class_id': fields.many2one('netpro.class', 'Class'),
        'product_plan_id': fields.many2one('netpro.product_plan_base', 'Product Plan'),
        'male_female_bamount': fields.float('Male / Female BAmount'),
        'occur_in_other_membership': fields.boolean('Occur in Other Membership'),
    }
netpro_membership_plan_employee()

class netpro_membership_plan_spouse(osv.osv):
    _name = 'netpro.membership_plan_spouse'
    _rec_name = 'class_id'
    _columns = {
        'class_id': fields.many2one('netpro.class', 'Class'),
        'product_plan_id': fields.many2one('netpro.product_plan_base', 'Product Plan'),
        'male_female_bamount': fields.float('Male / Female BAmount'),
        'occur_in_other_membership': fields.boolean('Occur in Other Membership'),
    }
netpro_membership_plan_spouse()

class netpro_membership_plan_child(osv.osv):
    _name = 'netpro.membership_plan_child'
    _rec_name = 'class_id'
    _columns = {
        'class_id': fields.many2one('netpro.class', 'Class'),
        'product_plan_id': fields.many2one('netpro.product_plan_base', 'Product Plan'),
        'male_female_bamount': fields.float('Male / Female BAmount'),
        'occur_in_other_membership': fields.boolean('Occur in Other Membership'),
    }
netpro_membership_plan_child()

class netpro_membership_plan_employee(osv.osv):
    _name = 'netpro.membership_plan_employee'
    _rec_name = 'class_id'
    _columns = {
        'class_id': fields.many2one('netpro.class', 'Class'),
        'product_plan_id': fields.many2one('netpro.product_plan_base', 'Product Plan'),
        'male_female_bamount': fields.float('Male / Female BAmount'),
        'occur_in_other_membership': fields.boolean('Occur in Other Membership'),
    }
netpro_membership_plan_employee()

class netpro_plan_schedule_detail_benefit_schedule(osv.osv):
    _name = 'netpro.plan_schedule_detail_benefit_schedule'
    _rec_name = 'plan_schedule_id'
    _columns = {
        'plan_schedule_id': fields.many2one('netpro.plan_schedule', 'Plan Schedule'),
        'product_plan_id': fields.many2one('netpro.product_plan_base', 'Product Plan'),
        'bamount': fields.float('BAmount'),
        'benefit_id': fields.many2one('netpro.benefit', 'Benefit ID'),
        'parent_benefit_id': fields.many2one('netpro.benefit', 'Parent Benefit'),
        'pre': fields.char('Pre'),
        'post': fields.char('Post'),
        'min_allowed': fields.float('Min Allowed'),
        'max_allowed': fields.float('Max Allowed'),
        'difference _provider_non_provider': fields.boolean('Difference Provider & Non Provider'),
        'not_affect_to_overall_limit': fields.boolean('Not Affect to Overall Limit'),
        'occurance_inner_limit': fields.boolean('Occurance Inner Limit'),
        'occurance_inner_limit_limit': fields.float('Limit'),
        'occurance_inner_limit_max': fields.float('Max'),
        'occurance_inner_limit_std': fields.float('Std.'),
        'confinement_inner_limit': fields.boolean('Confinement Inner Limit'),
        'confinement_inner_limit_limit': fields.float('Limit'),
        'confinement_inner_limit_max': fields.float('Max'),
        'confinement_inner_limit_std': fields.float('Std.'),
        'annual_inner_limit': fields.boolean('Annual Inner Limit'),
        'annual_inner_limit_limit': fields.float('Limit'),
        'annual_inner_limit_max': fields.float('Max'),
        'annual_inner_limit_std': fields.float('Std.'),
        'annual_inner_limit_family': fields.float('Family'),
        'annual_inner_limit_max_family': fields.float('Family Max'),
        'annual_inner_limit_std_family': fields.float('Family Std.'),
        'company_inner_limit': fields.boolean('Company Inner Limit'),
        'company_inner_limit_limit': fields.float('Limit'),
        'company_inner_limit_max': fields.float('Max'),
        'company_inner_limit_std': fields.float('Std.'),
        'company_inner_limit_reimbursement': fields.float('Reimbursement'),
        'company_inner_limit_seq_no': fields.integer('Seq. No.'),
        'non_provider_occurance_inner_limit': fields.boolean('Occurance Inner Limit'),
        'non_provider_occurance_inner_limit_limit': fields.float('Limit'),
        'non_provider_occurance_inner_limit_max': fields.float('Max'),
        'non_provider_occurance_inner_limit_std': fields.float('Std.'),
        'non_provider_confinement_inner_limit': fields.boolean('Confinement Inner Limit'),
        'non_provider_confinement_inner_limit_limit': fields.float('Limit'),
        'non_provider_confinement_inner_limit_max': fields.float('Max'),
        'non_provider_confinement_inner_limit_std': fields.float('Std.'),
        'non_provider_annual_inner_limit': fields.boolean('Annual Inner Limit'),
        'non_provider_annual_inner_limit_limit': fields.float('Limit'),
        'non_provider_annual_inner_limit_max': fields.float('Max'),
        'non_provider_annual_inner_limit_std': fields.float('Std.'),
        'non_provider_annual_inner_limit_family_limit': fields.float('Family'),
        'non_provider_annual_inner_limit_family_max': fields.float('Family Max'),
        'non_provider_annual_inner_limit_family_std': fields.float('Family Std.'),
        'non_provider_company_inner_limit': fields.boolean('Company Inner Limit'),
        'non_provider_company_inner_limit_limit': fields.float('Limit'),
        'non_provider_company_inner_limit_max': fields.float('Max'),
        'non_provider_company_inner_limit_std': fields.float('Std.'),
    }
netpro_plan_schedule_detail_benefit_schedule()

class netpro_plan_schedule_detail_diagnosis_exclusion(osv.osv):
    _name = 'netpro.plan_schedule_detail_diagnosis_exclusion'
    _rec_name = 'plan_schedule_id'
    _columns = {
        'plan_schedule_id': fields.many2one('netpro.plan_schedule', 'Plan Schedule'),
        'master_diagnosis_exclusion_id': fields.many2one('netpro.master_diagnosis_exclusion', 'Master Diagnosis Exclusion'),
        'description': fields.text('Description'),
    }
netpro_plan_schedule_detail_diagnosis_exclusion()

class netpro_plan_schedule_detail_diagnosis_exclusion_exception(osv.osv):
    _name = 'netpro.plan_schedule_detail_diagnosis_exclusion_exception'
    _rec_name = 'plan_schedule_id'
    _columns = {
        'plan_schedule_id': fields.many2one('netpro.plan_schedule', 'Plan Schedule'),
        'master_diagnosis_exclusion_id': fields.many2one('netpro.master_diagnosis_exclusion', 'Master Diagnosis Exclusion'),
        'description': fields.text('Description'),
    }
netpro_plan_schedule_detail_diagnosis_exclusion_exception()

# >>> pindah ke vit_actuary
# class netpro_benefit(osv.osv):
#     _name = 'netpro.benefit'
#     _columns = {
#         'benefit_id': fields.char('Benefit ID'),
#         'name': fields.char('Name'),
#         'as_parent': fields.boolean('As Parent'),
#     }
# netpro_benefit()

class netpro_master_diagnosis_exclusion(osv.osv):
    _name = 'netpro.master_diagnosis_exclusion'
    _rec_name = 'diagnosis_id'
    _columns = {
        'diagnosis_id': fields.char('Diagnosis ID'),
        'description': fields.text('Diagnosis Description'),
        'poly': fields.char('Poly'),
        'as_exception': fields.boolean('As Exception'),
    }
netpro_master_diagnosis_exclusion()

class netpro_correspondence_rule(osv.osv):
    _name = 'netpro.correspondence_rule'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_correspondence_rule()

class netpro_claim_rule(osv.osv):
    _name = 'netpro.claim_rule'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_claim_rule()

