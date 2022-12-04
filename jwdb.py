from peewee import *

database = MySQLDatabase('jwdb', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'localhost', 'port': 3307, 'user': 'root', 'password': ''})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class AppApp(BaseModel):
    app_id = CharField(column_name='appId')
    app_version = BigIntegerField(column_name='appVersion')
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    description = TextField(null=True)
    license = TextField(null=True)
    meta = TextField(null=True)
    name = CharField(index=True, null=True)
    published = UnknownField(null=True)  # bit

    class Meta:
        table_name = 'app_app'
        indexes = (
            (('app_id', 'app_version'), True),
        )
        primary_key = CompositeKey('app_id', 'app_version')

class AppBuilder(BaseModel):
    app = ForeignKeyField(column_name='appId', field='app_id', model=AppApp)
    app_version = ForeignKeyField(backref='app_app_app_version_set', column_name='appVersion', field='app_version', model=AppApp)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    description = TextField(null=True)
    id = CharField()
    json = TextField(null=True)
    name = CharField(index=True, null=True)
    type = CharField(index=True, null=True)

    class Meta:
        table_name = 'app_builder'
        indexes = (
            (('app', 'app_version', 'id'), True),
        )
        primary_key = CompositeKey('app', 'app_version', 'id')

class AppDatalist(BaseModel):
    app = ForeignKeyField(column_name='appId', field='app_id', model=AppApp)
    app_version = ForeignKeyField(backref='app_app_app_version_set', column_name='appVersion', field='app_version', model=AppApp)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    description = TextField(null=True)
    id = CharField()
    json = TextField(null=True)
    name = CharField(index=True, null=True)

    class Meta:
        table_name = 'app_datalist'
        indexes = (
            (('app', 'app_version'), False),
            (('app', 'app_version', 'id'), True),
        )
        primary_key = CompositeKey('app', 'app_version', 'id')

class AppEnvVariable(BaseModel):
    app = ForeignKeyField(column_name='appId', field='app_id', model=AppApp)
    app_version = ForeignKeyField(backref='app_app_app_version_set', column_name='appVersion', field='app_version', model=AppApp)
    id = CharField()
    remarks = TextField(null=True)
    value = TextField(null=True)

    class Meta:
        table_name = 'app_env_variable'
        indexes = (
            (('app', 'app_version'), False),
            (('app', 'app_version', 'id'), True),
        )
        primary_key = CompositeKey('app', 'app_version', 'id')

class AppFd(BaseModel):
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)

    class Meta:
        table_name = 'app_fd'

class AppFdAppcenter(BaseModel):
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_appcenter'

class AppFdApproveStatus(BaseModel):
    c_label = TextField(null=True)
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_approve_status'

class AppFdCase(BaseModel):
    c_field13 = TextField(null=True)
    c_initialization = TextField(null=True)
    c_label = TextField(null=True)
    c_pass_criteria = TextField(null=True)
    c_precondition = TextField(null=True)
    c_priority = TextField(null=True)
    c_results = TextField(null=True)
    c_stop_condition = TextField(null=True)
    c_title = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_case'

class AppFdCaseDesignMethod(BaseModel):
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_case_design_method'

class AppFdClosedThrough(BaseModel):
    c_detail = TextField(null=True)
    c_label = TextField(null=True)
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_closed_through'

class AppFdCodeLines(BaseModel):
    c_blank_lines = TextField(null=True)
    c_comment_ratio = TextField(null=True)
    c_mixed_lines = TextField(null=True)
    c_pure_code_lines = TextField(null=True)
    c_pure_comment_lines = TextField(null=True)
    c_total_code_lines = TextField(null=True)
    c_total_comment_lines = TextField(null=True)
    c_total_lines = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_code_lines'

class AppFdCodeScale(BaseModel):
    c_detail = TextField(null=True)
    c_label = TextField(null=True)
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_code_scale'

class AppFdCodingLanguage(BaseModel):
    c_language = TextField(null=True)
    c_release_version = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_coding_language'

class AppFdContractSubject(BaseModel):
    c_call_number = TextField(null=True)
    c_contact = TextField(null=True)
    c_corporate = TextField(null=True)
    c_corporate_representative = TextField(null=True)
    c_email = TextField(null=True)
    c_upload_attachments = TextField(null=True)
    c_upload_license = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_contract_subject'

class AppFdCorner(BaseModel):
    c_temperature = TextField(null=True)
    c_voltage = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_corner'

class AppFdCriticalLevel(BaseModel):
    c_harmful_consequence = TextField(null=True)
    c_hazard_level = TextField(null=True)
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_critical_level'

class AppFdDefect(BaseModel):
    c_category = TextField(null=True)
    c_closed_throuh = TextField(null=True)
    c_expectation = TextField(null=True)
    c_label = TextField(null=True)
    c_name = TextField(null=True)
    c_operation = TextField(null=True)
    c_proposal = TextField(null=True)
    c_related_dut = TextField(null=True)
    c_result = TextField(null=True)
    c_serverity = TextField(null=True)
    c_status = TextField(null=True)
    c_violated_rules = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_defect'

class AppFdDefectCategory(BaseModel):
    c_detail = TextField(null=True)
    c_label = TextField(null=True)
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_defect_category'

class AppFdDefectSeverity(BaseModel):
    c_detail = TextField(null=True)
    c_label = TextField(null=True)
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_defect_severity'

class AppFdDefectStatus(BaseModel):
    c_description = TextField(null=True)
    c_label = TextField(null=True)
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_defect_status'

class AppFdDesignRequirement(BaseModel):
    c_detail = TextField(null=True)
    c_label = TextField(null=True)
    c_title = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_design_requirement'

class AppFdDut(BaseModel):
    c_category = TextField(null=True)
    c_label = TextField(null=True)
    c_name = TextField(null=True)
    c_round = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_dut'

class AppFdDutCategory(BaseModel):
    c_label = TextField(null=True)
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_dut_category'

class AppFdEquipment(BaseModel):
    c_application = TextField(null=True)
    c_asset_number = TextField(null=True)
    c_feature = TextField(null=True)
    c_model = TextField(null=True)
    c_name = TextField(null=True)
    c_next_examine_date = TextField(null=True)
    c_owner = TextField(null=True)
    c_photo = TextField(null=True)
    c_vendor = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_equipment'

class AppFdExcuteState(BaseModel):
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_excute_state'

class AppFdExtremeCorner(BaseModel):
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_extreme_corner'

class AppFdFeature(BaseModel):
    c_case_design_method = TextField(null=True)
    c_expectation = TextField(null=True)
    c_granularity = TextField(null=True)
    c_test_method = TextField(null=True)
    c_title = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_feature'

class AppFdJChartData(BaseModel):
    c_parameter1 = TextField(null=True)
    c_parameter2 = TextField(null=True)
    c_parameter3 = TextField(null=True)
    c_value = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_chart_data'

class AppFdJCrmAccount(BaseModel):
    c_account_name = TextField(column_name='c_accountName', null=True)
    c_address = TextField(null=True)
    c_attachment = TextField(null=True)
    c_city = TextField(null=True)
    c_country = TextField(null=True)
    c_email = TextField(null=True)
    c_fax = TextField(null=True)
    c_office = TextField(null=True)
    c_state = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_crm_account'

class AppFdJCrmContact(BaseModel):
    c_account = TextField(null=True)
    c_address = TextField(null=True)
    c_address_available = TextField(column_name='c_addressAvailable', null=True)
    c_attachment = TextField(null=True)
    c_city = TextField(null=True)
    c_country = TextField(null=True)
    c_email = TextField(null=True)
    c_first_name = TextField(column_name='c_firstName', null=True)
    c_last_name = TextField(column_name='c_lastName', null=True)
    c_mobile = TextField(null=True)
    c_office = TextField(null=True)
    c_photo = TextField(null=True)
    c_state = TextField(null=True)
    c_title = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_crm_contact'

class AppFdJCrmOpportunity(BaseModel):
    c_account = TextField(null=True)
    c_amount = TextField(null=True)
    c_description = TextField(null=True)
    c_new_account = TextField(column_name='c_newAccount', null=True)
    c_source = TextField(null=True)
    c_stage = TextField(null=True)
    c_title = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_crm_opportunity'

class AppFdJCrmProposal(BaseModel):
    c_account = TextField(null=True)
    c_approver = TextField(null=True)
    c_attachment = TextField(null=True)
    c_comments = TextField(null=True)
    c_date_approved = TextField(column_name='c_dateApproved', null=True)
    c_date_proposed = TextField(column_name='c_dateProposed', null=True)
    c_description = TextField(null=True)
    c_notes = TextField(null=True)
    c_proposer = TextField(null=True)
    c_ref_no = TextField(column_name='c_refNo', null=True)
    c_select_approver = TextField(column_name='c_selectApprover', null=True)
    c_status = TextField(null=True)
    c_title = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_crm_proposal'

class AppFdJExpenseApproval(BaseModel):
    c_approved_by = TextField(column_name='c_ApprovedBy', null=True)
    c_approved_date = TextField(column_name='c_ApprovedDate', null=True)
    c_approver = TextField(null=True)
    c_claim = TextField(null=True)
    c_comment = TextField(null=True)
    c_username = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_expense_approval'

class AppFdJExpenseCat(BaseModel):
    c_category = TextField(column_name='c_Category', null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_expense_cat'

class AppFdJExpenseClaim(BaseModel):
    c_approved_by = TextField(column_name='c_ApprovedBy', null=True)
    c_approved_date = TextField(column_name='c_ApprovedDate', null=True)
    c_created_date = TextField(column_name='c_CreatedDate', null=True)
    c_finance_approved_by = TextField(column_name='c_FinanceApprovedBy', null=True)
    c_finance_approved_date = TextField(column_name='c_FinanceApprovedDate', null=True)
    c_select_approver = TextField(column_name='c_SelectApprover', null=True)
    c_approval_comments = TextField(null=True)
    c_claimant = TextField(null=True)
    c_finance_comments = TextField(null=True)
    c_receipt = TextField(null=True)
    c_ref = TextField(null=True)
    c_remark = TextField(null=True)
    c_sp_ecd = TextField(column_name='c_spECD', null=True)
    c_status = TextField(null=True)
    c_title = TextField(null=True)
    c_total = TextField(null=True)
    c_username = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_expense_claim'

class AppFdJExpenseEntry(BaseModel):
    c_amount = TextField(null=True)
    c_category = TextField(null=True)
    c_claim = TextField(null=True)
    c_date = TextField(null=True)
    c_purpose = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_expense_entry'

class AppFdJIsrRemark(BaseModel):
    c_name = TextField(null=True)
    c_remarks = TextField(null=True)
    c_request_id = TextField(null=True)
    c_username = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_isr_remark'

class AppFdJIsrRequest(BaseModel):
    c_assignee = TextField(null=True)
    c_attachment1 = TextField(null=True)
    c_attachment2 = TextField(null=True)
    c_attention = TextField(null=True)
    c_created_date = TextField(column_name='c_createdDate', null=True)
    c_date_verified = TextField(column_name='c_dateVerified', null=True)
    c_department = TextField(null=True)
    c_description = TextField(null=True)
    c_duedate = TextField(null=True)
    c_fg_r = TextField(column_name='c_fgR', null=True)
    c_priority = TextField(null=True)
    c_ref_id = TextField(null=True)
    c_remarks = TextField(null=True)
    c_requester = TextField(null=True)
    c_requester_name = TextField(null=True)
    c_status = TextField(null=True)
    c_subject = TextField(null=True)
    c_verifier = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_isr_request'

class AppFdJMeetingData(BaseModel):
    c_date = TextField(null=True)
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_meeting_data'

class AppFdJScGrid1(BaseModel):
    c_date = TextField(null=True)
    c_file = TextField(null=True)
    c_fk = TextField(null=True)
    c_name = TextField(null=True)
    c_select = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_sc_grid1'

class AppFdJScGrid2(BaseModel):
    c_date = TextField(null=True)
    c_file = TextField(null=True)
    c_fk = TextField(null=True)
    c_name = TextField(null=True)
    c_select = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_sc_grid2'

class AppFdJScGrid3(BaseModel):
    c_date = TextField(null=True)
    c_fk = TextField(null=True)
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_sc_grid3'

class AppFdJScGrid4(BaseModel):
    c_first_name = TextField(column_name='c_firstName', null=True)
    c_fk = TextField(null=True)
    c_last_name = TextField(column_name='c_lastName', null=True)
    c_username = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_sc_grid4'

class AppFdJScTran(BaseModel):
    c_approval_status1 = TextField(column_name='c_approvalStatus1', null=True)
    c_approval_status2 = TextField(column_name='c_approvalStatus2', null=True)
    c_approver_username1 = TextField(column_name='c_approverUsername1', null=True)
    c_approver_username2 = TextField(column_name='c_approverUsername2', null=True)
    c_page1_key = TextField(null=True)
    c_page2_key = TextField(null=True)
    c_page3_key = TextField(null=True)
    c_page4_key = TextField(null=True)
    c_rcounter = TextField(null=True)
    c_reason1 = TextField(null=True)
    c_reason2 = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_sc_tran'

class AppFdJScTranT1(BaseModel):
    c_calculation = TextField(null=True)
    c_date1 = TextField(null=True)
    c_date2 = TextField(null=True)
    c_date3 = TextField(null=True)
    c_date4 = TextField(null=True)
    c_date5 = TextField(null=True)
    c_date6 = TextField(null=True)
    c_ecounter = TextField(null=True)
    c_numeric1 = TextField(null=True)
    c_numeric2 = TextField(null=True)
    c_rich_text_editor = TextField(column_name='c_richTextEditor', null=True)
    c_signature = TextField(null=True)
    c_text_area = TextField(column_name='c_textArea', null=True)
    c_text_field = TextField(column_name='c_textField', null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_sc_tran_t1'

class AppFdJScTranT2(BaseModel):
    c_check_box = TextField(column_name='c_checkBox', null=True)
    c_ecounter = TextField(null=True)
    c_multi_select_box = TextField(column_name='c_multiSelectBox', null=True)
    c_popup_select_box = TextField(column_name='c_popupSelectBox', null=True)
    c_radio = TextField(null=True)
    c_select_box = TextField(column_name='c_selectBox', null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_sc_tran_t2'

class AppFdJScTranT3(BaseModel):
    c_ecounter = TextField(null=True)
    c_file_upload = TextField(column_name='c_fileUpload', null=True)
    c_image_upload = TextField(column_name='c_imageUpload', null=True)
    c_image_upload_1 = TextField(column_name='c_imageUpload_1', null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_sc_tran_t3'

class AppFdJScTranT4(BaseModel):
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_sc_tran_t4'

class AppFdJStock(BaseModel):
    c_closing = TextField(column_name='c_Closing', null=True)
    c_date = TextField(column_name='c_Date', null=True)
    c_highest = TextField(column_name='c_Highest', null=True)
    c_lowest = TextField(column_name='c_Lowest', null=True)
    c_open = TextField(column_name='c_Open', null=True)
    c_request_no = TextField(column_name='c_RequestNo', null=True)
    c_stock_code = TextField(column_name='c_StockCode', null=True)
    c_first_name = TextField(column_name='c_firstName', null=True)
    c_username = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_stock'

class AppFdJTemp(BaseModel):
    c_active = TextField(null=True)
    c_department = TextField(null=True)
    c_email = TextField(null=True)
    c_employee_code = TextField(column_name='c_employeeCode', null=True)
    c_end_date = TextField(column_name='c_endDate', null=True)
    c_first_name = TextField(column_name='c_firstName', null=True)
    c_grade = TextField(null=True)
    c_groups = TextField(null=True)
    c_is_hod = TextField(column_name='c_isHod', null=True)
    c_job_title = TextField(column_name='c_jobTitle', null=True)
    c_last_name = TextField(column_name='c_lastName', null=True)
    c_organization = TextField(null=True)
    c_password = TextField(null=True)
    c_report_to = TextField(column_name='c_reportTo', null=True)
    c_start_date = TextField(column_name='c_startDate', null=True)
    c_time_zone = TextField(column_name='c_timeZone', null=True)
    c_user_roles = TextField(column_name='c_userRoles', null=True)
    c_username = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_temp'

class AppFdJUserRegister(BaseModel):
    c_active = TextField(null=True)
    c_comments = TextField(null=True)
    c_email = TextField(null=True)
    c_first_name = TextField(column_name='c_firstName', null=True)
    c_last_name = TextField(column_name='c_lastName', null=True)
    c_password = TextField(null=True)
    c_status = TextField(null=True)
    c_user_roles = TextField(column_name='c_userRoles', null=True)
    c_username = TextField(null=True)
    c_verify_password = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_j_user_register'

class AppFdOrganization(BaseModel):
    c_address = TextField(null=True)
    c_call_number = TextField(null=True)
    c_contact = TextField(null=True)
    c_email = TextField(null=True)
    c_full_name = TextField(null=True)
    c_short_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_organization'

class AppFdOrganizatonCategory(BaseModel):
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_organizaton_category'

class AppFdPlatformType(BaseModel):
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_platform_type'

class AppFdPriority(BaseModel):
    c_label = TextField(null=True)
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_priority'

class AppFdProject(BaseModel):
    c_critical_level = TextField(null=True)
    c_data_from = TextField(null=True)
    c_date_to = TextField(null=True)
    c_label = TextField(null=True)
    c_languages = TextField(null=True)
    c_leader = TextField(null=True)
    c_member = TextField(null=True)
    c_name = TextField(null=True)
    c_platform_type = TextField(null=True)
    c_report_type = TextField(null=True)
    c_standards = TextField(null=True)
    c_test_level = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_project'

class AppFdQualityGrade(BaseModel):
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_quality_grade'

class AppFdReportType(BaseModel):
    c_alias_name = TextField(null=True)
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_report_type'

class AppFdResultCheck(BaseModel):
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_result_check'

class AppFdRound(BaseModel):
    c_date_from = TextField(null=True)
    c_date_to = TextField(null=True)
    c_label = TextField(null=True)
    c_name = TextField(null=True)
    c_package = TextField(null=True)
    c_project = TextField(null=True)
    c_quality_grade = TextField(null=True)
    c_speed_grade = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_round'

class AppFdSign(BaseModel):
    c_name = TextField(null=True)
    c_sign_date = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_sign'

class AppFdSignature(BaseModel):
    c_name = TextField(null=True)
    c_seal = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_signature'

class AppFdSoftware(BaseModel):
    c_application = TextField(null=True)
    c_name = TextField(null=True)
    c_release_version = TextField(null=True)
    c_vendor = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_software'

class AppFdStandard(BaseModel):
    c_label = TextField(null=True)
    c_name = TextField(null=True)
    c_release_date = TextField(null=True)
    c_released_by = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_standard'

class AppFdStep(BaseModel):
    c_excute_state = TextField(null=True)
    c_expectation = TextField(null=True)
    c_label = TextField(null=True)
    c_operation = TextField(null=True)
    c_result = TextField(null=True)
    c_result_check = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_step'

class AppFdTestLevel(BaseModel):
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_test_level'

class AppFdTestMethod(BaseModel):
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_test_method'

class AppFdTestRequiement(BaseModel):
    c_label = TextField(null=True)
    c_precondition = TextField(null=True)
    c_priority = TextField(null=True)
    c_stop_condition = TextField(null=True)
    c_sufficiency_criteria = TextField(null=True)
    c_test_type = TextField(null=True)
    c_title = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_test_requiement'

class AppFdTestType(BaseModel):
    c_label = TextField(null=True)
    c_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_test_type'

class AppFdTestingCenter(BaseModel):
    c_address = TextField(null=True)
    c_call_number = TextField(null=True)
    c_contact = TextField(null=True)
    c_email = TextField(null=True)
    c_full_name = TextField(null=True)
    c_short_name = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_testing_center'

class AppFdUploadIdcard(BaseModel):
    c_emblem = TextField(null=True)
    c_name = TextField(null=True)
    c_number = TextField(null=True)
    c_portrait = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_upload_idcard'

class AppFdVvBody(BaseModel):
    c_call_number = TextField(null=True)
    c_contact = TextField(null=True)
    c_corporate = TextField(null=True)
    c_email = TextField(null=True)
    created_by = CharField(column_name='createdBy', null=True)
    created_by_name = CharField(column_name='createdByName', null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    id = CharField(primary_key=True)
    modified_by = CharField(column_name='modifiedBy', null=True)
    modified_by_name = CharField(column_name='modifiedByName', null=True)

    class Meta:
        table_name = 'app_fd_vv_body'

class AppForm(BaseModel):
    app = ForeignKeyField(column_name='appId', field='app_id', model=AppApp)
    app_version = ForeignKeyField(backref='app_app_app_version_set', column_name='appVersion', field='app_version', model=AppApp)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    description = TextField(null=True)
    form_id = CharField(column_name='formId')
    json = TextField(null=True)
    name = CharField(index=True, null=True)
    table_name = CharField(column_name='tableName', null=True)

    class Meta:
        table_name = 'app_form'
        indexes = (
            (('app', 'app_version'), False),
            (('app', 'app_version', 'form_id'), True),
        )
        primary_key = CompositeKey('app', 'app_version', 'form_id')

class AppFormDataAuditTrail(BaseModel):
    action = CharField(null=True)
    app_id = CharField(column_name='appId', null=True)
    app_version = CharField(column_name='appVersion', null=True)
    data = TextField(null=True)
    datetime = DateTimeField(null=True)
    form_id = CharField(column_name='formId', null=True)
    id = CharField(primary_key=True)
    table_name = CharField(column_name='tableName', null=True)
    username = CharField(null=True)

    class Meta:
        table_name = 'app_form_data_audit_trail'

class AppMessage(BaseModel):
    app = ForeignKeyField(column_name='appId', field='app_id', model=AppApp)
    app_version = ForeignKeyField(backref='app_app_app_version_set', column_name='appVersion', field='app_version', model=AppApp)
    locale = CharField(null=True)
    message = TextField(null=True)
    message_key = CharField(column_name='messageKey', null=True)
    ouid = CharField()

    class Meta:
        table_name = 'app_message'
        indexes = (
            (('app', 'app_version'), False),
            (('app', 'app_version', 'ouid'), True),
        )
        primary_key = CompositeKey('app', 'app_version', 'ouid')

class AppPackage(BaseModel):
    app = ForeignKeyField(column_name='appId', field='app_id', model=AppApp, null=True)
    app_version = ForeignKeyField(backref='app_app_app_version_set', column_name='appVersion', field='app_version', model=AppApp, null=True)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    name = CharField(null=True)
    package_id = CharField(column_name='packageId')
    package_version = BigIntegerField(column_name='packageVersion')

    class Meta:
        table_name = 'app_package'
        indexes = (
            (('app', 'app_version'), False),
            (('package_id', 'package_version'), True),
        )
        primary_key = CompositeKey('package_id', 'package_version')

class AppPackageActivityForm(BaseModel):
    activity_def_id = CharField(column_name='activityDefId')
    auto_continue = UnknownField(column_name='autoContinue', null=True)  # bit
    disable_save_as_draft = UnknownField(column_name='disableSaveAsDraft', null=True)  # bit
    form_i_frame_style = CharField(column_name='formIFrameStyle', null=True)
    form_id = CharField(column_name='formId', null=True)
    form_url = CharField(column_name='formUrl', null=True)
    ouid = CharField(null=True)
    package = ForeignKeyField(column_name='packageId', field='package_id', model=AppPackage)
    package_version = ForeignKeyField(backref='app_package_package_version_set', column_name='packageVersion', field='package_version', model=AppPackage)
    process_def_id = CharField(column_name='processDefId')
    type = CharField(null=True)

    class Meta:
        table_name = 'app_package_activity_form'
        indexes = (
            (('package', 'package_version'), False),
            (('process_def_id', 'activity_def_id', 'package', 'package_version'), True),
        )
        primary_key = CompositeKey('activity_def_id', 'package', 'package_version', 'process_def_id')

class AppPackageActivityPlugin(BaseModel):
    activity_def_id = CharField(column_name='activityDefId')
    ouid = CharField(null=True)
    package = ForeignKeyField(column_name='packageId', field='package_id', model=AppPackage)
    package_version = ForeignKeyField(backref='app_package_package_version_set', column_name='packageVersion', field='package_version', model=AppPackage)
    plugin_name = CharField(column_name='pluginName', null=True)
    plugin_properties = TextField(column_name='pluginProperties', null=True)
    process_def_id = CharField(column_name='processDefId')

    class Meta:
        table_name = 'app_package_activity_plugin'
        indexes = (
            (('package', 'package_version'), False),
            (('process_def_id', 'activity_def_id', 'package', 'package_version'), True),
        )
        primary_key = CompositeKey('activity_def_id', 'package', 'package_version', 'process_def_id')

class AppPackageParticipant(BaseModel):
    ouid = CharField(null=True)
    package = ForeignKeyField(column_name='packageId', field='package_id', model=AppPackage)
    package_version = ForeignKeyField(backref='app_package_package_version_set', column_name='packageVersion', field='package_version', model=AppPackage)
    participant_id = CharField(column_name='participantId')
    plugin_properties = TextField(column_name='pluginProperties', null=True)
    process_def_id = CharField(column_name='processDefId')
    type = CharField(null=True)
    value = TextField(null=True)

    class Meta:
        table_name = 'app_package_participant'
        indexes = (
            (('package', 'package_version'), False),
            (('process_def_id', 'participant_id', 'package', 'package_version'), True),
        )
        primary_key = CompositeKey('package', 'package_version', 'participant_id', 'process_def_id')

class AppPluginDefault(BaseModel):
    app = ForeignKeyField(column_name='appId', field='app_id', model=AppApp)
    app_version = ForeignKeyField(backref='app_app_app_version_set', column_name='appVersion', field='app_version', model=AppApp)
    id = CharField()
    plugin_description = TextField(column_name='pluginDescription', null=True)
    plugin_name = CharField(column_name='pluginName', null=True)
    plugin_properties = TextField(column_name='pluginProperties', null=True)

    class Meta:
        table_name = 'app_plugin_default'
        indexes = (
            (('app', 'app_version'), False),
            (('app', 'app_version', 'id'), True),
        )
        primary_key = CompositeKey('app', 'app_version', 'id')

class AppReportApp(BaseModel):
    app_id = CharField(column_name='appId', null=True)
    app_name = CharField(column_name='appName', null=True)
    app_version = CharField(column_name='appVersion', null=True)
    uuid = CharField(primary_key=True)

    class Meta:
        table_name = 'app_report_app'

class AppReportPackage(BaseModel):
    app_uid = ForeignKeyField(column_name='appUid', field='uuid', model=AppReportApp, null=True)
    package_id = CharField(column_name='packageId', null=True)
    package_name = CharField(column_name='packageName', null=True)
    package_version = CharField(column_name='packageVersion', null=True)
    uuid = CharField(primary_key=True)

    class Meta:
        table_name = 'app_report_package'

class AppReportProcess(BaseModel):
    package_uid = ForeignKeyField(column_name='packageUid', field='uuid', model=AppReportPackage, null=True)
    process_def_id = CharField(column_name='processDefId', null=True)
    process_name = CharField(column_name='processName', null=True)
    uuid = CharField(primary_key=True)

    class Meta:
        table_name = 'app_report_process'

class AppReportActivity(BaseModel):
    activity_def_id = CharField(column_name='activityDefId', null=True)
    activity_name = CharField(column_name='activityName', null=True)
    process_uid = ForeignKeyField(column_name='processUid', field='uuid', model=AppReportProcess, null=True)
    uuid = CharField(primary_key=True)

    class Meta:
        table_name = 'app_report_activity'

class AppReportProcessInstance(BaseModel):
    delay = BigIntegerField(null=True)
    due = DateTimeField(null=True)
    finish_time = DateTimeField(column_name='finishTime', null=True)
    instance_id = CharField(column_name='instanceId', primary_key=True)
    process_uid = ForeignKeyField(column_name='processUid', field='uuid', model=AppReportProcess, null=True)
    requester = CharField(null=True)
    started_time = DateTimeField(column_name='startedTime', null=True)
    state = CharField(null=True)
    time_consuming_from_started_time = BigIntegerField(column_name='timeConsumingFromStartedTime', null=True)

    class Meta:
        table_name = 'app_report_process_instance'

class AppReportActivityInstance(BaseModel):
    activity_uid = ForeignKeyField(column_name='activityUid', field='uuid', model=AppReportActivity, null=True)
    assignment_users = TextField(column_name='assignmentUsers', null=True)
    created_time = DateTimeField(column_name='createdTime', null=True)
    delay = BigIntegerField(null=True)
    due = DateTimeField(null=True)
    finish_time = DateTimeField(column_name='finishTime', null=True)
    instance_id = CharField(column_name='instanceId', primary_key=True)
    name_of_accepted_user = CharField(column_name='nameOfAcceptedUser', null=True)
    performer = CharField(null=True)
    process_instance = ForeignKeyField(column_name='processInstanceId', field='instance_id', model=AppReportProcessInstance, null=True)
    started_time = DateTimeField(column_name='startedTime', null=True)
    state = CharField(null=True)
    status = CharField(null=True)
    time_consuming_from_created_time = BigIntegerField(column_name='timeConsumingFromCreatedTime', null=True)
    time_consuming_from_started_time = BigIntegerField(column_name='timeConsumingFromStartedTime', null=True)

    class Meta:
        table_name = 'app_report_activity_instance'

class AppResource(BaseModel):
    app = ForeignKeyField(column_name='appId', field='app_id', model=AppApp)
    app_version = ForeignKeyField(backref='app_app_app_version_set', column_name='appVersion', field='app_version', model=AppApp)
    filesize = BigIntegerField(null=True)
    id = CharField()
    permission_class = CharField(column_name='permissionClass', null=True)
    permission_properties = TextField(column_name='permissionProperties', null=True)

    class Meta:
        table_name = 'app_resource'
        indexes = (
            (('app', 'app_version', 'id'), True),
        )
        primary_key = CompositeKey('app', 'app_version', 'id')

class AppUserview(BaseModel):
    app = ForeignKeyField(column_name='appId', field='app_id', model=AppApp)
    app_version = ForeignKeyField(backref='app_app_app_version_set', column_name='appVersion', field='app_version', model=AppApp)
    date_created = DateTimeField(column_name='dateCreated', null=True)
    date_modified = DateTimeField(column_name='dateModified', null=True)
    description = TextField(null=True)
    id = CharField()
    json = TextField(null=True)
    name = CharField(index=True, null=True)

    class Meta:
        table_name = 'app_userview'
        indexes = (
            (('app', 'app_version'), False),
            (('app', 'app_version', 'id'), True),
        )
        primary_key = CompositeKey('app', 'app_version', 'id')

class DirOrganization(BaseModel):
    description = CharField(null=True)
    id = CharField(primary_key=True)
    name = CharField(null=True)
    parent = ForeignKeyField(column_name='parentId', field='id', model='self', null=True)

    class Meta:
        table_name = 'dir_organization'

class DirGrade(BaseModel):
    description = CharField(null=True)
    id = CharField(primary_key=True)
    name = CharField(null=True)
    organization = ForeignKeyField(column_name='organizationId', field='id', model=DirOrganization, null=True)

    class Meta:
        table_name = 'dir_grade'

# Possible reference cycle: dir_department
class DirUser(BaseModel):
    active = IntegerField(null=True)
    email = CharField(null=True)
    first_name = CharField(column_name='firstName', null=True)
    id = CharField(primary_key=True)
    last_name = CharField(column_name='lastName', null=True)
    locale = CharField(null=True)
    password = CharField(null=True)
    time_zone = CharField(column_name='timeZone', null=True)
    username = CharField(null=True)

    class Meta:
        table_name = 'dir_user'

class DirEmployment(BaseModel):
    employee_code = CharField(column_name='employeeCode', null=True)
    end_date = DateField(column_name='endDate', null=True)
    grade = ForeignKeyField(column_name='gradeId', field='id', model=DirGrade, null=True)
    id = CharField(primary_key=True)
    organization = ForeignKeyField(column_name='organizationId', field='id', model=DirOrganization, null=True)
    role = CharField(null=True)
    start_date = DateField(column_name='startDate', null=True)
    user = ForeignKeyField(column_name='userId', field='id', model=DirUser, null=True)
    #department = DeferredForeignKey(DirDepartment, column_name='departmentId', field='id', null=True) #还是报错不知道为什么
    departmentId = CharField(column_name='departmentId', null=True)

    class Meta:
        table_name = 'dir_employment'

class DirDepartment(BaseModel):
    description = CharField(null=True)
    hod = ForeignKeyField(column_name='hod', field='id', model=DirEmployment, null=True)
    id = CharField(primary_key=True)
    name = CharField(null=True)
    organization = ForeignKeyField(column_name='organizationId', field='id', model=DirOrganization, null=True)
    parent = ForeignKeyField(column_name='parentId', field='id', model='self', null=True)

    class Meta:
        table_name = 'dir_department'

class DirEmploymentReportTo(BaseModel):
    employment = ForeignKeyField(column_name='employmentId', field='id', model=DirEmployment)
    id = CharField(null=True)
    report_to = ForeignKeyField(backref='dir_employment_report_to_set', column_name='reportToId', field='id', model=DirEmployment)

    class Meta:
        table_name = 'dir_employment_report_to'
        indexes = (
            (('employment', 'report_to'), True),
        )
        primary_key = CompositeKey('employment', 'report_to')

class DirGroup(BaseModel):
    description = CharField(null=True)
    id = CharField(primary_key=True)
    name = CharField(null=True)
    organization = ForeignKeyField(column_name='organizationId', field='id', model=DirOrganization, null=True)

    class Meta:
        table_name = 'dir_group'

class DirRole(BaseModel):
    description = CharField(null=True)
    id = CharField(primary_key=True)
    name = CharField(null=True)

    class Meta:
        table_name = 'dir_role'

class DirUserExtra(BaseModel):
    algorithm = CharField(null=True)
    failedlogin_attempt = IntegerField(column_name='failedloginAttempt', null=True)
    last_loged_in_date = DateTimeField(column_name='lastLogedInDate', null=True)
    last_password_change_date = DateTimeField(column_name='lastPasswordChangeDate', null=True)
    lock_out_date = DateTimeField(column_name='lockOutDate', null=True)
    login_attempt = IntegerField(column_name='loginAttempt', null=True)
    no_password_expiration = UnknownField(column_name='noPasswordExpiration', null=True)  # bit
    required_password_change = UnknownField(column_name='requiredPasswordChange', null=True)  # bit
    username = CharField(primary_key=True)

    class Meta:
        table_name = 'dir_user_extra'

class DirUserGroup(BaseModel):
    group = ForeignKeyField(column_name='groupId', field='id', model=DirGroup)
    user = ForeignKeyField(column_name='userId', field='id', model=DirUser)

    class Meta:
        table_name = 'dir_user_group'
        indexes = (
            (('user', 'group'), True),
        )
        primary_key = CompositeKey('group', 'user')

class DirUserMeta(BaseModel):
    meta_key = CharField()
    meta_value = TextField(null=True)
    username = CharField()

    class Meta:
        table_name = 'dir_user_meta'
        indexes = (
            (('username', 'meta_key'), True),
        )
        primary_key = CompositeKey('meta_key', 'username')

class DirUserPasswordHistory(BaseModel):
    id = CharField(primary_key=True)
    password = CharField(null=True)
    salt = CharField(null=True)
    updated_date = DateTimeField(column_name='updatedDate', null=True)
    username = CharField(null=True)

    class Meta:
        table_name = 'dir_user_password_history'

class DirUserReplacement(BaseModel):
    app_id = CharField(column_name='appId', null=True)
    end_date = DateTimeField(column_name='endDate', null=True)
    id = CharField(primary_key=True)
    process_ids = CharField(column_name='processIds', null=True)
    replacement_user = CharField(column_name='replacementUser', null=True)
    start_date = DateTimeField(column_name='startDate', null=True)
    username = CharField(null=True)

    class Meta:
        table_name = 'dir_user_replacement'

class DirUserRole(BaseModel):
    role = ForeignKeyField(column_name='roleId', field='id', model=DirRole)
    user = ForeignKeyField(column_name='userId', field='id', model=DirUser)

    class Meta:
        table_name = 'dir_user_role'
        indexes = (
            (('user', 'role'), True),
        )
        primary_key = CompositeKey('role', 'user')

class Objectid(BaseModel):
    nextoid = DecimalField(primary_key=True)

    class Meta:
        table_name = 'objectid'

class Shkprocessdefinitions(BaseModel):
    name = CharField(column_name='Name', unique=True)
    package_id = CharField(column_name='PackageId')
    process_definition_created = BigIntegerField(column_name='ProcessDefinitionCreated')
    process_definition_id = CharField(column_name='ProcessDefinitionId')
    process_definition_version = CharField(column_name='ProcessDefinitionVersion')
    state = IntegerField(column_name='State')
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkprocessdefinitions'

class Shkprocessstates(BaseModel):
    key_value = CharField(column_name='KeyValue', unique=True)
    name = CharField(column_name='Name', unique=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkprocessstates'

class Shkprocesses(BaseModel):
    activity_requester_id = CharField(column_name='ActivityRequesterId', index=True, null=True)
    activity_requester_process_id = CharField(column_name='ActivityRequesterProcessId', null=True)
    created = BigIntegerField(column_name='Created')
    created_tzo = BigIntegerField(column_name='CreatedTZO')
    description = CharField(column_name='Description', null=True)
    external_requester_class_name = CharField(column_name='ExternalRequesterClassName', null=True)
    id = CharField(column_name='Id', unique=True)
    last_state_time = BigIntegerField(column_name='LastStateTime')
    last_state_time_tzo = BigIntegerField(column_name='LastStateTimeTZO')
    limit_time = BigIntegerField(column_name='LimitTime')
    limit_time_tzo = BigIntegerField(column_name='LimitTimeTZO')
    name = CharField(column_name='Name', null=True)
    p_def_name = CharField(column_name='PDefName')
    priority = IntegerField(column_name='Priority', null=True)
    process_definition = ForeignKeyField(column_name='ProcessDefinition', field='oid', model=Shkprocessdefinitions)
    resource_requester_id = CharField(column_name='ResourceRequesterId', index=True)
    started = BigIntegerField(column_name='Started', null=True)
    started_tzo = BigIntegerField(column_name='StartedTZO', null=True)
    state = ForeignKeyField(column_name='State', field='oid', model=Shkprocessstates)
    sync_version = BigIntegerField(column_name='SyncVersion')
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkprocesses'

class Shkactivitystates(BaseModel):
    key_value = CharField(column_name='KeyValue', unique=True)
    name = CharField(column_name='Name', unique=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkactivitystates'

class Shkresourcestable(BaseModel):
    name = CharField(column_name='Name', null=True)
    username = CharField(column_name='Username', unique=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkresourcestable'

class Shkactivities(BaseModel):
    accepted = BigIntegerField(column_name='Accepted', null=True)
    accepted_tzo = BigIntegerField(column_name='AcceptedTZO', null=True)
    activated = BigIntegerField(column_name='Activated')
    activated_tzo = BigIntegerField(column_name='ActivatedTZO')
    activity_definition_id = CharField(column_name='ActivityDefinitionId')
    activity_set_definition_id = CharField(column_name='ActivitySetDefinitionId', null=True)
    block_activity_id = CharField(column_name='BlockActivityId', null=True)
    description = CharField(column_name='Description', null=True)
    id = CharField(column_name='Id', unique=True)
    is_performer_asynchronous = IntegerField(column_name='IsPerformerAsynchronous', null=True)
    last_state_time = BigIntegerField(column_name='LastStateTime')
    last_state_time_tzo = BigIntegerField(column_name='LastStateTimeTZO')
    limit_time = BigIntegerField(column_name='LimitTime')
    limit_time_tzo = BigIntegerField(column_name='LimitTimeTZO')
    name = CharField(column_name='Name', null=True)
    p_def_name = CharField(column_name='PDefName')
    performer = CharField(column_name='Performer', null=True)
    priority = IntegerField(column_name='Priority', null=True)
    process = ForeignKeyField(column_name='Process', field='oid', model=Shkprocesses)
    process_id = CharField(column_name='ProcessId')
    resource_id = CharField(column_name='ResourceId', null=True)
    state = ForeignKeyField(column_name='State', field='oid', model=Shkactivitystates)
    the_resource = ForeignKeyField(column_name='TheResource', field='oid', model=Shkresourcestable, null=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkactivities'
        indexes = (
            (('process', 'activity_set_definition_id', 'activity_definition_id'), False),
            (('process', 'state'), False),
        )

class Shkactivitydata(BaseModel):
    activity = ForeignKeyField(column_name='Activity', field='oid', model=Shkactivities)
    cnt = DecimalField(column_name='CNT', unique=True)
    is_result = IntegerField(column_name='IsResult')
    ord_no = IntegerField(column_name='OrdNo')
    variable_definition_id = CharField(column_name='VariableDefinitionId')
    variable_type = IntegerField(column_name='VariableType')
    variable_value = TextField(column_name='VariableValue', null=True)
    variable_value_bool = IntegerField(column_name='VariableValueBOOL', null=True)
    variable_value_date = DateTimeField(column_name='VariableValueDATE', null=True)
    variable_value_dbl = FloatField(column_name='VariableValueDBL', null=True)
    variable_value_long = BigIntegerField(column_name='VariableValueLONG', null=True)
    variable_value_vchar = CharField(column_name='VariableValueVCHAR', null=True)
    variable_value_xml = TextField(column_name='VariableValueXML', null=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkactivitydata'
        indexes = (
            (('activity', 'variable_definition_id', 'ord_no'), True),
        )

class Shkactivitydatawob(BaseModel):
    activity = ForeignKeyField(column_name='Activity', field='oid', model=Shkactivities)
    cnt = DecimalField(column_name='CNT', unique=True)
    is_result = IntegerField(column_name='IsResult')
    ord_no = IntegerField(column_name='OrdNo')
    variable_definition_id = CharField(column_name='VariableDefinitionId')
    variable_type = IntegerField(column_name='VariableType')
    variable_value_bool = IntegerField(column_name='VariableValueBOOL', null=True)
    variable_value_date = DateTimeField(column_name='VariableValueDATE', null=True)
    variable_value_dbl = FloatField(column_name='VariableValueDBL', null=True)
    variable_value_long = BigIntegerField(column_name='VariableValueLONG', null=True)
    variable_value_vchar = CharField(column_name='VariableValueVCHAR', null=True)
    variable_value_xml = TextField(column_name='VariableValueXML', null=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkactivitydatawob'
        indexes = (
            (('activity', 'variable_definition_id', 'ord_no'), True),
        )

class Shkactivitydatablobs(BaseModel):
    activity_data_wob = ForeignKeyField(column_name='ActivityDataWOB', field='oid', model=Shkactivitydatawob)
    ord_no = IntegerField(column_name='OrdNo')
    variable_value = TextField(column_name='VariableValue', null=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkactivitydatablobs'
        indexes = (
            (('activity_data_wob', 'ord_no'), True),
        )

class Shkactivitystateeventaudits(BaseModel):
    key_value = CharField(column_name='KeyValue', unique=True)
    name = CharField(column_name='Name', unique=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkactivitystateeventaudits'

class Shkandjointable(BaseModel):
    activity = ForeignKeyField(column_name='Activity', field='oid', model=Shkactivities)
    activity_definition_id = CharField(column_name='ActivityDefinitionId')
    block_activity = ForeignKeyField(backref='shkactivities_block_activity_set', column_name='BlockActivity', field='oid', model=Shkactivities, null=True)
    cnt = DecimalField(column_name='CNT', unique=True)
    process = ForeignKeyField(column_name='Process', field='oid', model=Shkprocesses)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkandjointable'
        indexes = (
            (('process', 'block_activity', 'activity_definition_id'), False),
        )

class Shkeventtypes(BaseModel):
    key_value = CharField(column_name='KeyValue', unique=True)
    name = CharField(column_name='Name', unique=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkeventtypes'

class Shkassignmenteventaudits(BaseModel):
    activity_definition_id = CharField(column_name='ActivityDefinitionId')
    activity_definition_name = CharField(column_name='ActivityDefinitionName', null=True)
    activity_definition_type = IntegerField(column_name='ActivityDefinitionType')
    activity_id = CharField(column_name='ActivityId')
    activity_name = CharField(column_name='ActivityName', null=True)
    cnt = DecimalField(column_name='CNT', unique=True)
    is_accepted = IntegerField(column_name='IsAccepted')
    new_resource_name = CharField(column_name='NewResourceName', null=True)
    new_resource_username = CharField(column_name='NewResourceUsername')
    old_resource_name = CharField(column_name='OldResourceName', null=True)
    old_resource_username = CharField(column_name='OldResourceUsername', null=True)
    package_id = CharField(column_name='PackageId')
    process_definition_id = CharField(column_name='ProcessDefinitionId')
    process_definition_name = CharField(column_name='ProcessDefinitionName', null=True)
    process_factory_name = CharField(column_name='ProcessFactoryName')
    process_factory_version = CharField(column_name='ProcessFactoryVersion')
    process_id = CharField(column_name='ProcessId')
    process_name = CharField(column_name='ProcessName', null=True)
    recorded_time = BigIntegerField(column_name='RecordedTime')
    recorded_time_tzo = BigIntegerField(column_name='RecordedTimeTZO')
    the_type = ForeignKeyField(column_name='TheType', field='oid', model=Shkeventtypes)
    the_username = CharField(column_name='TheUsername')
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkassignmenteventaudits'

class Shkassignmentstable(BaseModel):
    activity = ForeignKeyField(column_name='Activity', field='oid', model=Shkactivities)
    activity = ForeignKeyField(backref='shkactivities_activity_set', column_name='ActivityId', field='id', model=Shkactivities)
    activity_process_def_name = CharField(column_name='ActivityProcessDefName')
    activity_process = ForeignKeyField(column_name='ActivityProcessId', field='id', model=Shkprocesses)
    cnt = DecimalField(column_name='CNT', unique=True)
    is_accepted = IntegerField(column_name='IsAccepted')
    is_valid = IntegerField(column_name='IsValid')
    resource_id = CharField(column_name='ResourceId', index=True)
    the_resource = ForeignKeyField(column_name='TheResource', field='oid', model=Shkresourcestable)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkassignmentstable'
        indexes = (
            (('activity', 'the_resource'), True),
            (('the_resource', 'is_valid'), False),
        )

class Shkcounters(BaseModel):
    name = CharField(unique=True)
    oid = DecimalField(primary_key=True)
    the_number = DecimalField()
    version = IntegerField()

    class Meta:
        table_name = 'shkcounters'

class Shkcreateprocesseventaudits(BaseModel):
    cnt = DecimalField(column_name='CNT', unique=True)
    p_activity_definition_id = CharField(column_name='PActivityDefinitionId', null=True)
    p_activity_definition_name = CharField(column_name='PActivityDefinitionName', null=True)
    p_activity_id = CharField(column_name='PActivityId', null=True)
    p_package_id = CharField(column_name='PPackageId', null=True)
    p_process_definition_id = CharField(column_name='PProcessDefinitionId', null=True)
    p_process_definition_name = CharField(column_name='PProcessDefinitionName', null=True)
    p_process_factory_name = CharField(column_name='PProcessFactoryName', null=True)
    p_process_factory_version = CharField(column_name='PProcessFactoryVersion', null=True)
    p_process_id = CharField(column_name='PProcessId', null=True)
    p_process_name = CharField(column_name='PProcessName', null=True)
    package_id = CharField(column_name='PackageId')
    process_definition_id = CharField(column_name='ProcessDefinitionId')
    process_definition_name = CharField(column_name='ProcessDefinitionName', null=True)
    process_factory_name = CharField(column_name='ProcessFactoryName')
    process_factory_version = CharField(column_name='ProcessFactoryVersion')
    process_id = CharField(column_name='ProcessId')
    process_name = CharField(column_name='ProcessName', null=True)
    recorded_time = BigIntegerField(column_name='RecordedTime')
    recorded_time_tzo = BigIntegerField(column_name='RecordedTimeTZO')
    the_type = ForeignKeyField(column_name='TheType', field='oid', model=Shkeventtypes)
    the_username = CharField(column_name='TheUsername')
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkcreateprocesseventaudits'

class Shkdataeventaudits(BaseModel):
    activity_definition_id = CharField(column_name='ActivityDefinitionId', null=True)
    activity_definition_name = CharField(column_name='ActivityDefinitionName', null=True)
    activity_definition_type = IntegerField(column_name='ActivityDefinitionType', null=True)
    activity_id = CharField(column_name='ActivityId', null=True)
    activity_name = CharField(column_name='ActivityName', null=True)
    cnt = DecimalField(column_name='CNT', unique=True)
    package_id = CharField(column_name='PackageId')
    process_definition_id = CharField(column_name='ProcessDefinitionId')
    process_definition_name = CharField(column_name='ProcessDefinitionName', null=True)
    process_factory_name = CharField(column_name='ProcessFactoryName')
    process_factory_version = CharField(column_name='ProcessFactoryVersion')
    process_id = CharField(column_name='ProcessId')
    process_name = CharField(column_name='ProcessName', null=True)
    recorded_time = BigIntegerField(column_name='RecordedTime')
    recorded_time_tzo = BigIntegerField(column_name='RecordedTimeTZO')
    the_type = ForeignKeyField(column_name='TheType', field='oid', model=Shkeventtypes)
    the_username = CharField(column_name='TheUsername')
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkdataeventaudits'

class Shkdeadlines(BaseModel):
    activity = ForeignKeyField(column_name='Activity', field='oid', model=Shkactivities)
    cnt = DecimalField(column_name='CNT', unique=True)
    exception_name = CharField(column_name='ExceptionName')
    is_executed = IntegerField(column_name='IsExecuted')
    is_synchronous = IntegerField(column_name='IsSynchronous')
    process = ForeignKeyField(column_name='Process', field='oid', model=Shkprocesses)
    time_limit = BigIntegerField(column_name='TimeLimit')
    time_limit_tzo = BigIntegerField(column_name='TimeLimitTZO')
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkdeadlines'
        indexes = (
            (('activity', 'time_limit'), False),
            (('process', 'time_limit'), False),
        )

class Shkgrouptable(BaseModel):
    description = CharField(null=True)
    groupid = CharField(unique=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkgrouptable'

class Shkgroupgrouptable(BaseModel):
    groupid = ForeignKeyField(column_name='groupid', field='oid', model=Shkgrouptable)
    oid = DecimalField(primary_key=True)
    sub_gid = ForeignKeyField(backref='shkgrouptable_sub_gid_set', column_name='sub_gid', field='oid', model=Shkgrouptable)
    version = IntegerField()

    class Meta:
        table_name = 'shkgroupgrouptable'
        indexes = (
            (('sub_gid', 'groupid'), True),
        )

class Shkgroupuser(BaseModel):
    username = CharField(column_name='USERNAME', unique=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkgroupuser'

class Shkxpdlparticipantpackage(BaseModel):
    package_id = CharField(column_name='PACKAGE_ID', unique=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkxpdlparticipantpackage'

class Shkpacklevelparticipant(BaseModel):
    packageoid = ForeignKeyField(column_name='PACKAGEOID', field='oid', model=Shkxpdlparticipantpackage)
    participant_id = CharField(column_name='PARTICIPANT_ID')
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkpacklevelparticipant'
        indexes = (
            (('participant_id', 'packageoid'), True),
        )

class Shkgroupuserpacklevelpart(BaseModel):
    participantoid = ForeignKeyField(column_name='PARTICIPANTOID', field='oid', model=Shkpacklevelparticipant)
    useroid = ForeignKeyField(column_name='USEROID', field='oid', model=Shkgroupuser)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkgroupuserpacklevelpart'
        indexes = (
            (('participantoid', 'useroid'), True),
        )

class Shkxpdlparticipantprocess(BaseModel):
    packageoid = ForeignKeyField(column_name='PACKAGEOID', field='oid', model=Shkxpdlparticipantpackage)
    process_id = CharField(column_name='PROCESS_ID')
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkxpdlparticipantprocess'
        indexes = (
            (('process_id', 'packageoid'), True),
        )

class Shkproclevelparticipant(BaseModel):
    participant_id = CharField(column_name='PARTICIPANT_ID')
    processoid = ForeignKeyField(column_name='PROCESSOID', field='oid', model=Shkxpdlparticipantprocess)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkproclevelparticipant'
        indexes = (
            (('participant_id', 'processoid'), True),
        )

class Shkgroupuserproclevelpart(BaseModel):
    participantoid = ForeignKeyField(column_name='PARTICIPANTOID', field='oid', model=Shkproclevelparticipant)
    useroid = ForeignKeyField(column_name='USEROID', field='oid', model=Shkgroupuser)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkgroupuserproclevelpart'
        indexes = (
            (('participantoid', 'useroid'), True),
        )

class Shkneweventauditdata(BaseModel):
    cnt = DecimalField(column_name='CNT', unique=True)
    data_event_audit = ForeignKeyField(column_name='DataEventAudit', field='oid', model=Shkdataeventaudits)
    ord_no = IntegerField(column_name='OrdNo')
    variable_definition_id = CharField(column_name='VariableDefinitionId')
    variable_type = IntegerField(column_name='VariableType')
    variable_value = TextField(column_name='VariableValue', null=True)
    variable_value_bool = IntegerField(column_name='VariableValueBOOL', null=True)
    variable_value_date = DateTimeField(column_name='VariableValueDATE', null=True)
    variable_value_dbl = FloatField(column_name='VariableValueDBL', null=True)
    variable_value_long = BigIntegerField(column_name='VariableValueLONG', null=True)
    variable_value_vchar = CharField(column_name='VariableValueVCHAR', null=True)
    variable_value_xml = TextField(column_name='VariableValueXML', null=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkneweventauditdata'
        indexes = (
            (('data_event_audit', 'variable_definition_id', 'ord_no'), True),
        )

class Shkneweventauditdatawob(BaseModel):
    cnt = DecimalField(column_name='CNT', unique=True)
    data_event_audit = ForeignKeyField(column_name='DataEventAudit', field='oid', model=Shkdataeventaudits)
    ord_no = IntegerField(column_name='OrdNo')
    variable_definition_id = CharField(column_name='VariableDefinitionId')
    variable_type = IntegerField(column_name='VariableType')
    variable_value_bool = IntegerField(column_name='VariableValueBOOL', null=True)
    variable_value_date = DateTimeField(column_name='VariableValueDATE', null=True)
    variable_value_dbl = FloatField(column_name='VariableValueDBL', null=True)
    variable_value_long = BigIntegerField(column_name='VariableValueLONG', null=True)
    variable_value_vchar = CharField(column_name='VariableValueVCHAR', null=True)
    variable_value_xml = TextField(column_name='VariableValueXML', null=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkneweventauditdatawob'
        indexes = (
            (('data_event_audit', 'variable_definition_id', 'ord_no'), True),
        )

class Shkneweventauditdatablobs(BaseModel):
    new_event_audit_data_wob = ForeignKeyField(column_name='NewEventAuditDataWOB', field='oid', model=Shkneweventauditdatawob)
    ord_no = IntegerField(column_name='OrdNo')
    variable_value = TextField(column_name='VariableValue', null=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkneweventauditdatablobs'
        indexes = (
            (('new_event_audit_data_wob', 'ord_no'), True),
        )

class Shknextxpdlversions(BaseModel):
    next_version = CharField(column_name='NextVersion')
    xpdl_id = CharField(column_name='XPDLId')
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shknextxpdlversions'
        indexes = (
            (('xpdl_id', 'next_version'), True),
        )

class Shknormaluser(BaseModel):
    username = CharField(column_name='USERNAME', unique=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shknormaluser'

class Shkoldeventauditdata(BaseModel):
    cnt = DecimalField(column_name='CNT', unique=True)
    data_event_audit = ForeignKeyField(column_name='DataEventAudit', field='oid', model=Shkdataeventaudits)
    ord_no = IntegerField(column_name='OrdNo')
    variable_definition_id = CharField(column_name='VariableDefinitionId')
    variable_type = IntegerField(column_name='VariableType')
    variable_value = TextField(column_name='VariableValue', null=True)
    variable_value_bool = IntegerField(column_name='VariableValueBOOL', null=True)
    variable_value_date = DateTimeField(column_name='VariableValueDATE', null=True)
    variable_value_dbl = FloatField(column_name='VariableValueDBL', null=True)
    variable_value_long = BigIntegerField(column_name='VariableValueLONG', null=True)
    variable_value_vchar = CharField(column_name='VariableValueVCHAR', null=True)
    variable_value_xml = TextField(column_name='VariableValueXML', null=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkoldeventauditdata'
        indexes = (
            (('data_event_audit', 'variable_definition_id', 'ord_no'), True),
        )

class Shkoldeventauditdatawob(BaseModel):
    cnt = DecimalField(column_name='CNT', unique=True)
    data_event_audit = ForeignKeyField(column_name='DataEventAudit', field='oid', model=Shkdataeventaudits)
    ord_no = IntegerField(column_name='OrdNo')
    variable_definition_id = CharField(column_name='VariableDefinitionId')
    variable_type = IntegerField(column_name='VariableType')
    variable_value_bool = IntegerField(column_name='VariableValueBOOL', null=True)
    variable_value_date = DateTimeField(column_name='VariableValueDATE', null=True)
    variable_value_dbl = FloatField(column_name='VariableValueDBL', null=True)
    variable_value_long = BigIntegerField(column_name='VariableValueLONG', null=True)
    variable_value_vchar = CharField(column_name='VariableValueVCHAR', null=True)
    variable_value_xml = TextField(column_name='VariableValueXML', null=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkoldeventauditdatawob'
        indexes = (
            (('data_event_audit', 'variable_definition_id', 'ord_no'), True),
        )

class Shkoldeventauditdatablobs(BaseModel):
    old_event_audit_data_wob = ForeignKeyField(column_name='OldEventAuditDataWOB', field='oid', model=Shkoldeventauditdatawob)
    ord_no = IntegerField(column_name='OrdNo')
    variable_value = TextField(column_name='VariableValue', null=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkoldeventauditdatablobs'
        indexes = (
            (('old_event_audit_data_wob', 'ord_no'), True),
        )

class Shkxpdlapplicationpackage(BaseModel):
    package_id = CharField(column_name='PACKAGE_ID', unique=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkxpdlapplicationpackage'

class Shkpacklevelxpdlapp(BaseModel):
    application_id = CharField(column_name='APPLICATION_ID')
    packageoid = ForeignKeyField(column_name='PACKAGEOID', field='oid', model=Shkxpdlapplicationpackage)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkpacklevelxpdlapp'
        indexes = (
            (('application_id', 'packageoid'), True),
        )

class Shktoolagentapp(BaseModel):
    app_name = CharField(column_name='APP_NAME')
    tool_agent_name = CharField(column_name='TOOL_AGENT_NAME')
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shktoolagentapp'
        indexes = (
            (('tool_agent_name', 'app_name'), True),
        )

class Shktoolagentappdetail(BaseModel):
    app_mode = DecimalField(column_name='APP_MODE')
    toolagent_appoid = ForeignKeyField(column_name='TOOLAGENT_APPOID', field='oid', model=Shktoolagentapp)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shktoolagentappdetail'
        indexes = (
            (('app_mode', 'toolagent_appoid'), True),
        )

class Shkpacklevelxpdlapptaappdetail(BaseModel):
    toolagentoid = ForeignKeyField(column_name='TOOLAGENTOID', field='oid', model=Shktoolagentappdetail)
    xpdl_appoid = ForeignKeyField(column_name='XPDL_APPOID', field='oid', model=Shkpacklevelxpdlapp)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkpacklevelxpdlapptaappdetail'
        indexes = (
            (('xpdl_appoid', 'toolagentoid'), True),
        )

class Shktoolagentuser(BaseModel):
    pwd = CharField(column_name='PWD', null=True)
    username = CharField(column_name='USERNAME', unique=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shktoolagentuser'

class Shktoolagentappdetailuser(BaseModel):
    toolagent_appoid = ForeignKeyField(column_name='TOOLAGENT_APPOID', field='oid', model=Shktoolagentappdetail)
    useroid = ForeignKeyField(column_name='USEROID', field='oid', model=Shktoolagentuser)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shktoolagentappdetailuser'
        indexes = (
            (('toolagent_appoid', 'useroid'), True),
        )

class Shkpacklevelxpdlapptaappdetusr(BaseModel):
    toolagentoid = ForeignKeyField(column_name='TOOLAGENTOID', field='oid', model=Shktoolagentappdetailuser)
    xpdl_appoid = ForeignKeyField(column_name='XPDL_APPOID', field='oid', model=Shkpacklevelxpdlapp)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkpacklevelxpdlapptaappdetusr'
        indexes = (
            (('xpdl_appoid', 'toolagentoid'), True),
        )

class Shktoolagentappuser(BaseModel):
    toolagent_appoid = ForeignKeyField(column_name='TOOLAGENT_APPOID', field='oid', model=Shktoolagentapp)
    useroid = ForeignKeyField(column_name='USEROID', field='oid', model=Shktoolagentuser)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shktoolagentappuser'
        indexes = (
            (('toolagent_appoid', 'useroid'), True),
        )

class Shkpacklevelxpdlapptaappuser(BaseModel):
    toolagentoid = ForeignKeyField(column_name='TOOLAGENTOID', field='oid', model=Shktoolagentappuser)
    xpdl_appoid = ForeignKeyField(column_name='XPDL_APPOID', field='oid', model=Shkpacklevelxpdlapp)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkpacklevelxpdlapptaappuser'
        indexes = (
            (('xpdl_appoid', 'toolagentoid'), True),
        )

class Shkpacklevelxpdlapptoolagntapp(BaseModel):
    toolagentoid = ForeignKeyField(column_name='TOOLAGENTOID', field='oid', model=Shktoolagentapp)
    xpdl_appoid = ForeignKeyField(column_name='XPDL_APPOID', field='oid', model=Shkpacklevelxpdlapp)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkpacklevelxpdlapptoolagntapp'
        indexes = (
            (('xpdl_appoid', 'toolagentoid'), True),
        )

class Shkprocessdata(BaseModel):
    cnt = DecimalField(column_name='CNT', unique=True)
    ord_no = IntegerField(column_name='OrdNo')
    process = ForeignKeyField(column_name='Process', field='oid', model=Shkprocesses)
    variable_definition_id = CharField(column_name='VariableDefinitionId')
    variable_type = IntegerField(column_name='VariableType')
    variable_value = TextField(column_name='VariableValue', null=True)
    variable_value_bool = IntegerField(column_name='VariableValueBOOL', null=True)
    variable_value_date = DateTimeField(column_name='VariableValueDATE', null=True)
    variable_value_dbl = FloatField(column_name='VariableValueDBL', null=True)
    variable_value_long = BigIntegerField(column_name='VariableValueLONG', null=True)
    variable_value_vchar = CharField(column_name='VariableValueVCHAR', null=True)
    variable_value_xml = TextField(column_name='VariableValueXML', null=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkprocessdata'
        indexes = (
            (('process', 'variable_definition_id', 'ord_no'), True),
        )

class Shkprocessdatawob(BaseModel):
    cnt = DecimalField(column_name='CNT', unique=True)
    ord_no = IntegerField(column_name='OrdNo')
    process = ForeignKeyField(column_name='Process', field='oid', model=Shkprocesses)
    variable_definition_id = CharField(column_name='VariableDefinitionId')
    variable_type = IntegerField(column_name='VariableType')
    variable_value_bool = IntegerField(column_name='VariableValueBOOL', null=True)
    variable_value_date = DateTimeField(column_name='VariableValueDATE', null=True)
    variable_value_dbl = FloatField(column_name='VariableValueDBL', null=True)
    variable_value_long = BigIntegerField(column_name='VariableValueLONG', null=True)
    variable_value_vchar = CharField(column_name='VariableValueVCHAR', null=True)
    variable_value_xml = TextField(column_name='VariableValueXML', null=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkprocessdatawob'
        indexes = (
            (('process', 'variable_definition_id', 'ord_no'), True),
        )

class Shkprocessdatablobs(BaseModel):
    ord_no = IntegerField(column_name='OrdNo')
    process_data_wob = ForeignKeyField(column_name='ProcessDataWOB', field='oid', model=Shkprocessdatawob)
    variable_value = TextField(column_name='VariableValue', null=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkprocessdatablobs'
        indexes = (
            (('process_data_wob', 'ord_no'), True),
        )

class Shkprocessrequesters(BaseModel):
    activity_requester = ForeignKeyField(column_name='ActivityRequester', field='oid', model=Shkactivities, null=True)
    id = CharField(column_name='Id', unique=True)
    resource_requester = ForeignKeyField(column_name='ResourceRequester', field='oid', model=Shkresourcestable, null=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkprocessrequesters'

class Shkprocessstateeventaudits(BaseModel):
    key_value = CharField(column_name='KeyValue', unique=True)
    name = CharField(column_name='Name', unique=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkprocessstateeventaudits'

class Shkxpdlapplicationprocess(BaseModel):
    packageoid = ForeignKeyField(column_name='PACKAGEOID', field='oid', model=Shkxpdlapplicationpackage)
    process_id = CharField(column_name='PROCESS_ID')
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkxpdlapplicationprocess'
        indexes = (
            (('process_id', 'packageoid'), True),
        )

class Shkproclevelxpdlapp(BaseModel):
    application_id = CharField(column_name='APPLICATION_ID')
    processoid = ForeignKeyField(column_name='PROCESSOID', field='oid', model=Shkxpdlapplicationprocess)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkproclevelxpdlapp'
        indexes = (
            (('application_id', 'processoid'), True),
        )

class Shkproclevelxpdlapptaappdetail(BaseModel):
    toolagentoid = ForeignKeyField(column_name='TOOLAGENTOID', field='oid', model=Shktoolagentappdetail)
    xpdl_appoid = ForeignKeyField(column_name='XPDL_APPOID', field='oid', model=Shkproclevelxpdlapp)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkproclevelxpdlapptaappdetail'
        indexes = (
            (('xpdl_appoid', 'toolagentoid'), True),
        )

class Shkproclevelxpdlapptaappdetusr(BaseModel):
    toolagentoid = ForeignKeyField(column_name='TOOLAGENTOID', field='oid', model=Shktoolagentappdetailuser)
    xpdl_appoid = ForeignKeyField(column_name='XPDL_APPOID', field='oid', model=Shkproclevelxpdlapp)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkproclevelxpdlapptaappdetusr'
        indexes = (
            (('xpdl_appoid', 'toolagentoid'), True),
        )

class Shkproclevelxpdlapptaappuser(BaseModel):
    toolagentoid = ForeignKeyField(column_name='TOOLAGENTOID', field='oid', model=Shktoolagentappuser)
    xpdl_appoid = ForeignKeyField(column_name='XPDL_APPOID', field='oid', model=Shkproclevelxpdlapp)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkproclevelxpdlapptaappuser'
        indexes = (
            (('xpdl_appoid', 'toolagentoid'), True),
        )

class Shkproclevelxpdlapptoolagntapp(BaseModel):
    toolagentoid = ForeignKeyField(column_name='TOOLAGENTOID', field='oid', model=Shktoolagentapp)
    xpdl_appoid = ForeignKeyField(column_name='XPDL_APPOID', field='oid', model=Shkproclevelxpdlapp)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkproclevelxpdlapptoolagntapp'
        indexes = (
            (('xpdl_appoid', 'toolagentoid'), True),
        )

class Shkstateeventaudits(BaseModel):
    activity_definition_id = CharField(column_name='ActivityDefinitionId', null=True)
    activity_definition_name = CharField(column_name='ActivityDefinitionName', null=True)
    activity_definition_type = IntegerField(column_name='ActivityDefinitionType', null=True)
    activity_id = CharField(column_name='ActivityId', null=True)
    activity_name = CharField(column_name='ActivityName', null=True)
    cnt = DecimalField(column_name='CNT', unique=True)
    new_activity_state = ForeignKeyField(column_name='NewActivityState', field='oid', model=Shkactivitystateeventaudits, null=True)
    new_process_state = ForeignKeyField(column_name='NewProcessState', field='oid', model=Shkprocessstateeventaudits, null=True)
    old_activity_state = ForeignKeyField(backref='shkactivitystateeventaudits_old_activity_state_set', column_name='OldActivityState', field='oid', model=Shkactivitystateeventaudits, null=True)
    old_process_state = ForeignKeyField(backref='shkprocessstateeventaudits_old_process_state_set', column_name='OldProcessState', field='oid', model=Shkprocessstateeventaudits, null=True)
    package_id = CharField(column_name='PackageId')
    process_definition_id = CharField(column_name='ProcessDefinitionId')
    process_definition_name = CharField(column_name='ProcessDefinitionName', null=True)
    process_factory_name = CharField(column_name='ProcessFactoryName')
    process_factory_version = CharField(column_name='ProcessFactoryVersion')
    process_id = CharField(column_name='ProcessId')
    process_name = CharField(column_name='ProcessName', null=True)
    recorded_time = BigIntegerField(column_name='RecordedTime')
    recorded_time_tzo = BigIntegerField(column_name='RecordedTimeTZO')
    the_type = ForeignKeyField(column_name='TheType', field='oid', model=Shkeventtypes)
    the_username = CharField(column_name='TheUsername')
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkstateeventaudits'

class Shkusertable(BaseModel):
    email = CharField(null=True)
    firstname = CharField(null=True)
    lastname = CharField(null=True)
    oid = DecimalField(primary_key=True)
    passwd = CharField()
    userid = CharField(unique=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkusertable'

class Shkusergrouptable(BaseModel):
    groupid = ForeignKeyField(column_name='groupid', field='oid', model=Shkgrouptable)
    oid = DecimalField(primary_key=True)
    userid = ForeignKeyField(column_name='userid', field='oid', model=Shkusertable)
    version = IntegerField()

    class Meta:
        table_name = 'shkusergrouptable'
        indexes = (
            (('userid', 'groupid'), True),
        )

class Shkuserpacklevelpart(BaseModel):
    participantoid = ForeignKeyField(column_name='PARTICIPANTOID', field='oid', model=Shkpacklevelparticipant)
    useroid = ForeignKeyField(column_name='USEROID', field='oid', model=Shknormaluser)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkuserpacklevelpart'
        indexes = (
            (('participantoid', 'useroid'), True),
        )

class Shkuserproclevelparticipant(BaseModel):
    participantoid = ForeignKeyField(column_name='PARTICIPANTOID', field='oid', model=Shkproclevelparticipant)
    useroid = ForeignKeyField(column_name='USEROID', field='oid', model=Shknormaluser)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkuserproclevelparticipant'
        indexes = (
            (('participantoid', 'useroid'), True),
        )

class Shkxpdls(BaseModel):
    xpdl_class_version = BigIntegerField(column_name='XPDLClassVersion')
    xpdl_id = CharField(column_name='XPDLId')
    xpdl_upload_time = DateTimeField(column_name='XPDLUploadTime')
    xpdl_version = CharField(column_name='XPDLVersion')
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkxpdls'
        indexes = (
            (('xpdl_id', 'xpdl_version'), True),
        )

class Shkxpdldata(BaseModel):
    cnt = DecimalField(column_name='CNT', unique=True)
    xpdl = ForeignKeyField(column_name='XPDL', field='oid', model=Shkxpdls, unique=True)
    xpdl_class_content = TextField(column_name='XPDLClassContent', null=True)
    xpdl_content = TextField(column_name='XPDLContent', null=True)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkxpdldata'

class Shkxpdlhistory(BaseModel):
    xpdl_class_version = BigIntegerField(column_name='XPDLClassVersion')
    xpdl_history_upload_time = DateTimeField(column_name='XPDLHistoryUploadTime')
    xpdl_id = CharField(column_name='XPDLId')
    xpdl_upload_time = DateTimeField(column_name='XPDLUploadTime')
    xpdl_version = CharField(column_name='XPDLVersion')
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkxpdlhistory'
        indexes = (
            (('xpdl_id', 'xpdl_version'), True),
        )

class Shkxpdlhistorydata(BaseModel):
    cnt = DecimalField(column_name='CNT', unique=True)
    xpdl_class_content = TextField(column_name='XPDLClassContent')
    xpdl_content = TextField(column_name='XPDLContent')
    xpdl_history = ForeignKeyField(column_name='XPDLHistory', field='oid', model=Shkxpdlhistory)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkxpdlhistorydata'

class Shkxpdlreferences(BaseModel):
    referred_xpdl_id = CharField(column_name='ReferredXPDLId')
    referred_xpdl_number = IntegerField(column_name='ReferredXPDLNumber')
    referring_xpdl = ForeignKeyField(column_name='ReferringXPDL', field='oid', model=Shkxpdls)
    oid = DecimalField(primary_key=True)
    version = IntegerField()

    class Meta:
        table_name = 'shkxpdlreferences'
        indexes = (
            (('referred_xpdl_id', 'referring_xpdl'), True),
        )

class WfAuditTrail(BaseModel):
    app_id = CharField(column_name='appId', null=True)
    app_version = CharField(column_name='appVersion', null=True)
    clazz = CharField(null=True)
    id = CharField(primary_key=True)
    message = TextField(null=True)
    method = CharField(null=True)
    timestamp = DateTimeField(null=True)
    username = CharField(null=True)

    class Meta:
        table_name = 'wf_audit_trail'

class WfProcessLink(BaseModel):
    origin_process_id = CharField(column_name='originProcessId', null=True)
    parent_process_id = CharField(column_name='parentProcessId', null=True)
    process_id = CharField(column_name='processId', primary_key=True)

    class Meta:
        table_name = 'wf_process_link'

class WfReportPackage(BaseModel):
    package_id = CharField(column_name='packageId', primary_key=True)
    package_name = CharField(column_name='packageName', null=True)

    class Meta:
        table_name = 'wf_report_package'

class WfReportProcess(BaseModel):
    process_def_id = CharField(column_name='processDefId', primary_key=True)
    process_name = CharField(column_name='processName', null=True)
    version = CharField(null=True)

    class Meta:
        table_name = 'wf_report_process'

class WfReportActivity(BaseModel):
    activity_def_id = CharField(column_name='activityDefId', primary_key=True)
    activity_name = CharField(column_name='activityName', null=True)
    description = CharField(null=True)
    priority = CharField(null=True)

    class Meta:
        table_name = 'wf_report_activity'

class WfReport(BaseModel):
    activity_def = ForeignKeyField(column_name='activityDefId', field='activity_def_id', model=WfReportActivity, null=True)
    activity_instance_id = CharField(column_name='activityInstanceId', primary_key=True)
    app_id = CharField(column_name='appId', null=True)
    app_version = BigIntegerField(column_name='appVersion', null=True)
    assignment_users = TextField(column_name='assignmentUsers', null=True)
    created_time = DateTimeField(column_name='createdTime', null=True)
    date_limit = BigIntegerField(column_name='dateLimit', null=True)
    delay = BigIntegerField(null=True)
    due = DateTimeField(null=True)
    finish_time = DateTimeField(column_name='finishTime', null=True)
    name_of_accepted_user = CharField(column_name='nameOfAcceptedUser', null=True)
    package = ForeignKeyField(column_name='packageId', field='package_id', model=WfReportPackage, null=True)
    performer = CharField(null=True)
    priority = CharField(null=True)
    process_def = ForeignKeyField(column_name='processDefId', field='process_def_id', model=WfReportProcess, null=True)
    process_instance_id = CharField(column_name='processInstanceId', null=True)
    started_time = DateTimeField(column_name='startedTime', null=True)
    state = CharField(null=True)
    status = CharField(null=True)
    time_consuming_from_date_created = BigIntegerField(column_name='timeConsumingFromDateCreated', null=True)
    time_consuming_from_date_started = BigIntegerField(column_name='timeConsumingFromDateStarted', null=True)

    class Meta:
        table_name = 'wf_report'

class WfResourceBundleMessage(BaseModel):
    id = CharField(primary_key=True)
    locale = CharField(null=True)
    message = TextField(null=True)
    message_key = CharField(column_name='messageKey', null=True)

    class Meta:
        table_name = 'wf_resource_bundle_message'

class WfSetup(BaseModel):
    id = CharField(primary_key=True)
    ordering = IntegerField(null=True)
    property = CharField(null=True)
    value = TextField(null=True)

    class Meta:
        table_name = 'wf_setup'

