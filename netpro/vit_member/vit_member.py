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
class netpro_member(osv.osv):
    _name = 'netpro.member'
    _inherit = 'res.partner'
    _columns = {
        'policy_id': fields.many2one('netpro.policy', 'Policy', required=True),
        'insurance_period_start': fields.date('Insurance Period Start', required=True),
        'insurance_period_end': fields.date('Insurance Period End', required=True),
        'member_no': fields.char('Member No.', required=True),
        #'name': fields.char('Name', required=True),
        #'employee_id': fields.many2one('hr.employee', 'Employee', required=True),
        'census_no': fields.integer('Census No.'),
        'sex': fields.many2one('netpro.sex', 'Sex'),
        'marital_status': fields.many2one('netpro.marital_status', 'Marital Status'),
        #'email': fields.char('Email'),
        'mobile_phone': fields.char('Mobile Phone'),
        'date_of_birth': fields.date('DOB'),
        'age': fields.integer('Age'),
        'birth_place': fields.char('Birth Place'),
        'salary': fields.float('Salary'),
        'vip': fields.boolean('VIP'),
        'black_listed': fields.boolean('Black Listed '),
        'hold_car_swipe_claim': fields.boolean('Hold Card Swipe And Claim'),
        'remarks': fields.text('Remarks'),
        'class_id': fields.many2one('netpro.class', 'Class'),
        'membership': fields.many2one('netpro.membership', 'Membership'),
        'card_no': fields.char('Card No'),
        'register_no': fields.char('Register No.'),
        'period_start': fields.date('Period Start'),
        'period_end': fields.date('Period End'),
        'stnc': fields.date('STNC'),
        'group_id': fields.char('Group ID'),
        'payor_id': fields.many2one('netpro.payor', 'Payor'),
        'premium_type_id': fields.many2one('netpro.premium_type', 'Premium Type'),
        'area_id': fields.many2one('netpro.area', 'Area'),
        #'country_id': fields.many2one('netpro.country', 'Country'),
        'pre_existing_waived': fields.boolean('Pre Existing Waived'),
        'exclude_this_member': fields.boolean('Exclude this Member'),
        'dummy_member': fields.boolean('Dummy Member'),
        'mno': fields.float('MNO', readonly=True),
        'pmno': fields.integer('PMNO', readonly=True),
        'status': fields.char('Status', readonly=True),
        'trans_type': fields.char('Trans. Type', readonly=True),
        'suspend_tpa': fields.boolean('Suspend TPA', readonly=True),
        'account_no': fields.char('Account No'),
        'account_name': fields.char('Account Name'),
        'bank': fields.char('Bank'),
        'bank_name': fields.char('Bank Name'),
        'bank_branch': fields.char('Bank Branch'),
        #'company_name': fields.char('Company Name'),
        'company_address': fields.text('Address'),
        'title': fields.char('Title'),
        'division': fields.char('Division'),
        'branch': fields.char('Branch'),
        'occupation': fields.char('Occupation'),
        'id_no': fields.char('ID No'),
        #'personal_address': fields.text('Address'),
        #'city': fields.char('City'),
        'province': fields.char('Province'),
        #'zip_code': fields.char('ZIP Code'),
        #'phone': fields.char('Phone'),
        #'mobile': fields.char('Mobile'),
        #'fax': fields.char('Fax'),
        #'email': fields.char('Email'),
        'height': fields.integer('Height'),
        'weight': fields.integer('Weight'),
        'member_plan_ids': fields.one2many('netpro.member_plan', 'member_id', 'Plans', ondelete='cascade'),
        'family_ids': fields.one2many('netpro.member', 'parent_id', 'Families', ondelete='cascade'),
        'claim_history_ids': fields.one2many('netpro.member_claim_history', 'member_id', 'Claim Histories', ondelete='cascade'),
        'parent_id': fields.many2one('netpro.member', 'Family'),
    }
netpro_member()

# pindah ke vit_actuary

# class netpro_policy(osv.osv):
#     _name = 'netpro.policy'
#     _inherit = 'netpro.policy'
#     _columns = {
#         'member_ids' : fields.one2many('netpro.member', 'policy_id', 'Members', ondelete='cascade')
#     }
# netpro_policy()

# class netpro_product(osv.osv):
#     _name = 'netpro.product'
#     _columns = {
#         'code': fields.char('Product Code'),
#         'name': fields.char('Name'),
#         'alternative_name': fields.char('Name (alt)'),
#         'short_name': fields.char('Short Name'),
#         'description': fields.text('Description'),
#         'alternative_description': fields.text('Description (alt)'),
#         'rider': fields.boolean('Rider'),
#         'age_band_id': fields.many2one('netpro.age_band', 'Age Band'),
#         'sub_class': fields.many2one('netpro.toc', 'Sub Class'),
#         'product_type_id': fields.many2one('netpro.product_type', 'Product Type'),
#         'min_member': fields.integer('Min. Member'),
#         'max_age_coverage': fields.integer('Max. Age Coverage'),
#         'release_date': fields.date('Release Date'),
#         'status': fields.char('Status'),
#         'provider_limit': fields.float('Provider Limit'),
#         'reimbursement_limit': fields.float('Reimbursement Limit'),
#         'allowed_changing_inner_limit': fields.boolean('Allowed Changing Inner Limit'),
#         'allowed_changing_overall_limit': fields.boolean('Allowed Changing Overall Limit'),
#         'benefit_ids': fields.one2many('netpro.product_benefit', 'product_id', 'Benefits', ondelete='cascade'),
#         'term_condition_ids': fields.one2many('netpro.product_term_condition', 'product_id', 'Term And Condition', ondelete='cascade'),
#     }
# netpro_product()

#   class netpro_age_band(osv.osv):
#     _name = 'netpro.age_band'
#     _columns = {
#         'band_id': fields.integer('Band ID'),
#         'age_lower': fields.integer('Age Lower'),
#         'age_upper': fields.integer('Age Upper'),
#         'loading': fields.integer('Loading'),
#     }
# netpro_age_band()

# class netpro_term_condition(osv.osv):
#     _name = 'netpro.term_condition'
#     _columns = {
#         'tc_id': fields.char('TC ID'),
#         'name': fields.text('TC Name'),
#     }
# netpro_term_condition()

# class netpro_product_term_condition(osv.osv):
#     _name = 'netpro.product_term_condition'
#     _rec_name = 'product_id'
#     _columns = {
#         'product_id': fields.many2one('netpro.product', 'Product'),
#         'term_condition_id': fields.many2one('netpro.term_condition', 'Term And Condition'),
#     }
# netpro_product_term_condition()

# class netpro_product_benefit(osv.osv):
#     _name = 'netpro.product_benefit'
#     _rec_name = 'product_id'
#     _columns = {
#         'product_id': fields.many2one('netpro.product', 'Product'),
#         'benefit_id': fields.many2one('netpro.benefit', 'Benefit'),
#     }
# netpro_product_benefit()

# class netpro_product_plan(osv.osv):
#     _name = 'netpro.product_plan'
#     _columns = {
#         'code': fields.char('Product Plan Code'),
#         'name': fields.char('Name'),
#         'short_name': fields.char('Short Name'),
#         'description': fields.text('Description'),
#         'product_id': fields.many2one('netpro.product', 'Product Code'),
#         'currency_id': fields.many2one('res.currency', 'Currency'),
#         'product_plan_base_id': fields.many2one('netpro.product_plan_base', 'Product Plan'),
#         'overall_limit': fields.float('Overall Limit'),
#         'family_overall_limit': fields.float('Family Overall Limit'),
#         'remarks_ind': fields.text('Remarks (Ind)'),
#         'remarks_eng': fields.text('Remarks (Eng)'),
#         'no_refund': fields.boolean('No Refund'),
#         'no_refund_if_already_claim': fields.boolean('No Refund If Already Claim'),
#         'by_premium_table': fields.boolean('By Premium Table'),
#         'by_membership_classification': fields.boolean('By Membership Classification'),
#         'benefit_limit_affect_to_calculation': fields.boolean('Benefit Limit Affect to Calculation'),
#         'rate_calculation_after_loading': fields.boolean('Rate Calculation After Loading'),
#         'reimbusement_affect_to_premium': fields.boolean('Reimbursement Affect To Premium'),
#         'card_fee': fields.float('Card Fee'),
#         'inner_limit_apply_card_fee': fields.boolean('Apply Card Fee'),
#         'inner_limit_dependant_rate_base_on_male': fields.boolean('Dependant Rate base on Male'),
#         'inner_limit_limit_rate': fields.float('Limit Rate'),
#         'inner_limit_claim_rate': fields.float('Claim Rate'),
#         'inner_limit_annual_rate': fields.float('Annual Rate'),
#         'inner_limit_overall_limit_loading': fields.float('Overall Limit Loading'),
#         'as_charge_apply_card_fee': fields.boolean('Apply Card Fee'),
#         'as_charge_dependant_rate_base_on_male': fields.boolean('Dependant Rate base on Male'),
#         'as_charge_limit_rate': fields.float('Limit Rate'),
#         'as_charge_claim_rate': fields.float('Claim Rate'),
#         'as_charge_annual_rate': fields.float('Annual Rate'),
#         'as_charge_overall_limit_loading': fields.float('Overall Limit Loading'),
#         'sub_as_charge_apply_card_fee': fields.boolean('Apply Card Fee'),
#         'sub_as_charge_dependant_rate_base_on_male': fields.boolean('Dependant Rate base on Male'),
#         'sub_as_charge_limit_rate': fields.float('Limit Rate'),
#         'sub_as_charge_claim_rate': fields.float('Claim Rate'),
#         'sub_as_charge_annual_rate': fields.float('Annual Rate'),
#         'sub_as_charge_overall_limit_loading': fields.float('Overall Limit Loading'),
#         'benefit_ids': fields.one2many('netpro.product_plan_benefit', 'product_plan_id', 'Benefits', ondelete='cascade'),
#         'membership_ids': fields.one2many('netpro.product_plan_membership', 'product_plan_id', 'Memberships', ondelete='cascade'),
#         'premium_type_ids': fields.one2many('netpro.product_plan_premium_type', 'product_plan_id', 'Premium Type', ondelete='cascade'),
#     }
# netpro_product_plan()

# class netpro_product_plan_benefit(osv.osv):
#     _name = 'netpro.product_plan_benefit'
#     _rec_name = 'product_plan_id'
#     _columns = {
#         'product_plan_id': fields.many2one('netpro.product_plan', 'Product Plan'),
#         'benefit_id': fields.many2one('netpro.benefit', 'Benefit'),
#         'benefit_limit_start': fields.float('Benefit Limit Start'),
#         'benefit_limit_end': fields.float('Benefit Limit End'),
#         'parent_benefit_id': fields.many2one('netpro.benefit', 'Parent Benefit'),
#         'reimbursement': fields.float('Reimbursement'),
#         'benefit_seq_no': fields.integer('Benefit Seq No.'),
#         'limit_from_main_benefit_start': fields.float('Limit From Main Benefit Start'),
#         'limit_from_main_benefit_end': fields.float('Limit From Main Benefit End'),
#         'limit_from_annual_start': fields.float('Limit From Annual Start'),
#         'limit_from_annual_end': fields.float('Limit From Annual End'),
#         'annual_limit_after_loading': fields.boolean('Annual Limit After Loading'),
#         'average_benefit_rate_and_annual_rate': fields.boolean('Average Benefit Rate And Annual Rate'),
#         'not_effect_to_overall_limit': fields.boolean('Not Effect To Overall Limit'),
#         'default_benefit': fields.boolean('Default Benefit'),
#         'provider_per_occurance': fields.boolean('Per Occurance'),
#         'provider_per_occurance_amount_limit_1': fields.float('Amount Limit 1'),
#         'provider_per_occurance_amount_limit_2': fields.float('Amount Limit 2'),
#         'provider_per_occurance_amount_limit_3': fields.integer('Amount Limit 3'),
#         'provider_per_occurance_freq_limit': fields.integer('Freq Limit'),
#         'provider_per_confinement': fields.boolean('Per Confinement'),
#         'provider_per_confinement_amount_limit_1': fields.float('Amount Limit 1'),
#         'provider_per_confinement_amount_limit_2': fields.float('Amount Limit 2'),
#         'provider_per_confinement_amount_limit_3': fields.integer('Amount Limit 3'),
#         'provider_per_confinement_freq_limit': fields.integer('Freq Limit'),
#         'provider_per_year': fields.boolean('Per Year'),
#         'provider_per_year_amount_limit_1': fields.float('Amount Limit 1'),
#         'provider_per_year_amount_limit_2': fields.float('Amount Limit 2'),
#         'provider_per_year_amount_limit_3': fields.integer('Amount Limit 3'),
#         'provider_per_year_freq_limit': fields.integer('Freq Limit'),
#         'provider_per_year_family_amt_limit_1': fields.float('Family Amt. Limit'),
#         'provider_per_year_family_amt_limit_2': fields.float('Family Amt. Limit 2'),
#         'provider_per_year_family_amt_limit_3': fields.integer('Family Amt. Limit 3'),
#         'provider_per_year_family_freq_limit': fields.integer('Family Freq Limit'),
#         'provider_per_company': fields.boolean('Per Company'),
#         'provider_per_company_amount_limit_1': fields.float('Amount Limit 1'),
#         'provider_per_company_amount_limit_2': fields.float('Amount Limit 2'),
#         'provider_per_company_amount_limit_3': fields.integer('Amount Limit 3'),
#         'provider_per_company_freq_limit': fields.integer('Freq Limit'),
#         'non_provider_per_occurance': fields.boolean('Per Occurance'),
#         'non_provider_per_occurance_amount_limit_1': fields.float('Amount Limit 1'),
#         'non_provider_per_occurance_amount_limit_2': fields.float('Amount Limit 2'),
#         'non_provider_per_occurance_amount_limit_3': fields.integer('Amount Limit 3'),
#         'non_provider_per_occurance_freq_limit': fields.integer('Freq Limit'),
#         'non_provider_per_confinement': fields.boolean('Per Confinement'),
#         'non_provider_per_confinement_amount_limit_1': fields.float('Amount Limit 1'),
#         'non_provider_per_confinement_amount_limit_2': fields.float('Amount Limit 2'),
#         'non_provider_per_confinement_amount_limit_3': fields.integer('Amount Limit 3'),
#         'non_provider_per_confinement_freq_limit': fields.integer('Freq Limit'),
#         'non_provider_per_year': fields.boolean('Per Year'),
#         'non_provider_per_year_amount_limit_1': fields.float('Amount Limit 1'),
#         'non_provider_per_year_amount_limit_2': fields.float('Amount Limit 2'),
#         'non_provider_per_year_amount_limit_3': fields.integer('Amount Limit 3'),
#         'non_provider_per_year_family_amt_limit_1': fields.float('Family Amt. Limit 1'),
#         'non_provider_per_year_family_amt_limit_2': fields.float('Family Amt. Limit 2'),
#         'non_provider_per_year_family_amt_limit_3': fields.integer('Family Amt. Limit 3'),
#         'non_provider_per_year_family_freq_limit': fields.integer('Family Freq Limit'),
#         'non_provider_per_company': fields.boolean('Per Company'),
#         'non_provider_per_company_amount_limit_1': fields.float('Amount Limit 1'),
#         'non_provider_per_company_amount_limit_2': fields.float('Amount Limit 2'),
#         'non_provider_per_company_amount_limit_3': fields.integer('Amount Limit 3'),
#         'non_provider_per_company_freq_limit': fields.integer('Freq Limit'),
#     }
# netpro_product_plan_benefit()

# class netpro_product_plan_membership(osv.osv):
#     _name = 'netpro.product_plan_membership'
#     _rec_name = 'product_plan_id'
#     _columns = {
#         'product_plan_id': fields.many2one('netpro.product_plan', 'Product Plan'),
#         'membership_id': fields.many2one('netpro.membership', 'Membership'),
#         'gender_id': fields.many2one('netpro.gender', 'Gender'),
#         'marital_status_id': fields.many2one('netpro.marital_status', 'Marital Status'),
#     }
# netpro_product_plan_membership()

# class netpro_product_plan_premium_type(osv.osv):
#     _name = 'netpro.product_plan_premium_type'
#     _rec_name = 'product_plan_id'
#     _columns = {
#         'product_plan_id': fields.many2one('netpro.product_plan', 'Product Plan'),
#         'premium_type_id': fields.many2one('netpro.premium_type', 'Premium Type'),
#         'premium_table_id': fields.many2one('netpro.premium_table', 'Premium Table'),
#         'apply_to_policy_holder': fields.boolean('Apply To Policy Holder'),
#         'apply_to_spouse': fields.boolean('Apply To Spouse'),
#         'apply_to_children': fields.boolean('Apply To Children'),
#     }
# netpro_product_plan_premium_type()

# class netpro_premium_type(osv.osv):
#     _name = 'netpro.premium_type'
#     _columns = {
#         'name': fields.char('Name'),
#         'description': fields.text('Description'),
#     }
# netpro_premium_type()

# class netpro_premium_table(osv.osv):
#     _name = 'netpro.premium_table'
#     _columns = {
#         'name': fields.char('Name'),
#         'description': fields.text('Description'),
#     }
# netpro_premium_table()

# pindah ke actuary
# class netpro_membership(osv.osv):
#     _name = 'netpro.membership'
#     _columns = {
#         'membership_id': fields.char('Membership ID'),
#         'name_e': fields.char('Name (E)'),
#         'name_i': fields.char('Name (I)'),
#         'category': fields.char('Category'),
#         'age_between_start': fields.integer('Age Between Start'),
#         'age_between_end': fields.integer('Age Between End'),
#         'policy_owner': fields.boolean('Policy Owner'),
#         'allowed': fields.boolean('Allowed'),
#     }
# netpro_membership()

class netpro_gender(osv.osv):
    _name = 'netpro.gender'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_gender()

class netpro_marital_status(osv.osv):
    _name = 'netpro.marital_status'
    _columns = {
        'name': fields.char('Name'),
        'description': fields.text('Description'),
    }
netpro_marital_status()

class netpro_member_plan(osv.osv):
    _name = 'netpro.member_plan'
    _rec_name = 'member_id'
    _columns = {
        'member_id': fields.many2one('netpro.member', 'Member'),
        'plan_schedule_id': fields.many2one('netpro.plan_schedule', 'PPlan'),
        'product_plan'  : fields.related('plan_schedule_id', 'product_plan_base_id' , type="many2one", relation="netpro.product_plan_base", string="Product Plan", store=True),
        # 'product_plan': fields.related('plan_schedule_id', 'product_plan_base_id', type='many2one', string='Product Plan', store=True, readonly=True),
        'bamount': fields.float('BAmount'),
        'plan_limit': fields.float('Plan Limit'),
        'remaining_limit': fields.float('Remaining Limit'),
        'family_limit': fields.float('Family Limit'),
        'family_remaining_limit': fields.float('Family Remaining Limit'),
        'hi_plan': fields.boolean('Hi Plan'),
        'aso': fields.boolean('ASO'),
        'excess': fields.char('Excess'),
        'per_disability': fields.boolean('Per Disability'),
        'member_plan_detail_ids': fields.one2many('netpro.member_plan_detail', 'member_plan_id', 'Member Plan Details', ondelete='cascade'),
    }
netpro_member_plan()

class netpro_member_plan_detail(osv.osv):
    _name = 'netpro.member_plan_detail'
    _columns = {
        'member_plan_id': fields.many2one('netpro.member_plan', 'Member Plan'),
        'detail_id': fields.char('ID'),
        'name': fields.char('Name'),
        'reim': fields.float('Reim'),
        'provider_limit': fields.float('Provider Limit'),
        'non_provider_limit': fields.float('Non Provider Limit'),
        'unit': fields.char('Unit'),
        'usage': fields.float('Usage'),
        'remaining': fields.float('Remaining'),
    }
netpro_member_plan_detail()

class netpro_member_claim_history(osv.osv):
    _name = 'netpro.member_claim_history'
    _columns = {
        'member_id': fields.many2one('netpro.member', 'Member'),
        'claim_id': fields.many2one('netpro.claim', 'Claim'),
    }
netpro_member_claim_history()