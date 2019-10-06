DATASERVICE:

    • @api_technician_company.route('/<id_company>/technician', methods=['GET'])
      def technician_company_id(id_company):
      """
        endpoint which is used to find the technicians of a given company in the database
        :param id_company: company_id
        :return: return the technician referred to the id_company
      """
    • @api_technician_company.route('/technician/<id_technician>/add_chat_id/<chat_id>', methods=['GET'])
      def update_chat_id(id_technician, chat_id):
      """
       endpoint which is used to login the technician
       :param id_technician: id_technician, chat_id: chat_id
        :return: insert in the database the chat_id referred to the id_technician
      """
    • @api_technician_company.route('/technician_chat/<chat_id>/logout', methods=['GET'])
      def logout_chat_id(chat_id):
      """
        endpoint which is used to logout the technician
        :param chat_id: chat_id
        :return: when technician logout cancel the chat_id referred to the technician with the same chat_id
      """
    • @api_technician_company.route('/technician_chat/<chat_id>/update/<status>', methods=['GET'])
      def update_status_tech_by_chat_id(chat_id, status):
      """
        endpoint which is used to update the status of technician referred to chat_id
        :param chat_id: chat_id, status: status
      :return: update the status of technician referred to chat_id
      """
    • @api_technician_company.route('/technician/<tech_id>/update/<status>', methods=['GET'])
      def update_status_tech_by_tech_id(tech_id, status):
      """
        endpoint which is used to update the status of technician referred to tech_id
        :param tech_id: tech_id, status: status
       :return: update the status of technician referred to tech_id
      """
    • @api_technician_company.route('/technician_chat/<chat_id>/info', methods=['GET'])
       def get_tech_info_by_chat_id(chat_id):
       """
        endpoint which is used to select the information of technician by chat id
        :param chat_id: chat_id
        :return: return the information of technician by chat id
       """
    • @api_technician_company.route('/technician/<tech_id>/info', methods=['GET'])
      def get_tech_info_by_tech_id(tech_id):
      """
        endpoint which is used to select the information of technician by chat id
        :param tech_id: chat_id
        :return: return the information of technician by chat id
      """
    • @api_new.route('/add_new_condominium', methods=['POST'])
      def add_new_condominium():
      """
        endpoint which is used add a new condominium to database
        :param
        :return: add a new condominium to database and return the id of the condominium that has been added
      """
    • @api_new.route('/add_new_call', methods=['POST'])
      def add_new_call():
       """
        endpoint which is used add a new call to database
        :param
        :return: add a new call to database and return the id of the call that has been added
      """
    • @api_condominium_company.route('/<id_company>/condominium', methods=['GET'])
      def condominium_company_id(id_company):
       """
        endpoint which is used add a new call to database
        :param id_company: id_company
        :return: add a new call to database and return the id of the call that has been added
       """
    • @api_condominium.route('/<id_company>/number_condominium', methods=['GET'])
      def number_condominium_company_id(id_company):
       """
        endpoint which is used to have the number of condominium of company that has a certain id
        :param id_company: id_company
        :return: return the number of condominium of company that has a certain id
       """
    • @api_condominium.route('/number_condominium', methods=['GET'])
      def number_condominium():
      """
        endpoint which is used to have the number of condominium of all company
        :param
        :return: return the number of condominium of all company
      """
    • @api_condominium.route('/condominium/<build_id>', methods=['GET'])
      def condominium_by_id(build_id):
      """
            endpoint which is used to have the information of the condominiums that have a certain id
            :param build_id: build_id
            :return: return the information of the condominiums that have a certain id
      """
    • @api_companies.route('/companies', methods=['GET'])
      def companies():
      """
            endpoint which is used to have the informations of all the companies in the database
            :param
            :return: return the informations of all the companies in the database
      """
    • @api_calls.route('/companies/calls/<year>/<month>/<day>', methods=['GET'])
      def day_call(year, month, day):
      """
            endpoint which is used to have the calls of a specific date for all companies
            :params year: year, month: month, day: day
            :return: return the calls of a specific date for all companies
      """
    • @api_calls.route('/<id_company>/calls/<year>/<month>/<day>', methods=['GET'])
      def day_call_company(id_company, year, month, day):
      """
            endpoint which is used to have the calls of a specific date for a specific company
            :params id_company: id_company, year: year, month: month, day: day
            :return: return the calls of a specific date for a specific company
      """
    • @api_call_status.route('/companies/calls/<call_status_id>', methods=['GET'])
      def status(call_status_id):
      """
            endpoint which is used to have the calls of a specific status for all companies
            :params call_status_id: call_status_id
            :return: return the calls of a specific status for all companies
      """
    • @api_calls.route('/calls/<company_id>/<status>', methods=['GET'])
      def calls_company_by_status(company_id, status):
      """
            endpoint which is used to have calls of a specific company with a specific status
            :params company_id: company_id, status: status
            :return: return the calls of a specific company with a specific status
      """
    • @api_call_status.route('/calls/<call_id>/update/<status>/<id_technician>', methods=['GET'])
      def update_status(call_id, status, id_technician):
      """
            endpoint which is used to update the id call and assigns the call of a specific technician
            :params call_id: call_id, status: status, id_technician: id_technician
            :return: update the id call and assigns the call of a specific technician
      """
    • @api_call_status.route('/calls/active/tech/<tech_id>', methods=['GET'])
      def call_by_tech(tech_id):
       """
            endpoint which is used to active a specific technician
            :params tech_id: tech_id
            :return: active a specific technician
       """



BUSINESS LOGIC:

    • @api_technician_company_business.route('/<id_company>/technician', methods=['GET'])
      def technician_company_business(id_company):
      """
            endpoint which is used to have the technician of a specific company
            :params id_company: id_company
            :return: return the technician of a specific company
      """
    • @api_technician_company_business.route('/technician/<id_technician>/add_chat_id/<chat_id>', methods=['GET'])
      def update_chat_id(id_technician, chat_id):
      """
            endpoint which is used to add the chat_id of a specific technician
            :params id_chat: id_chat
            :return: add the chat_id of a specific technician
      """
    • @api_technician_company_business.route('/technician_chat/<chat_id>/logout', methods=['GET'])
      def logout_chat_id(chat_id):
      """
            endpoint which is used to a specific technician to logout
            :params id_chat: id_chat
            :return: add the chat_id of a specific technician
      """
    • @api_technician_company_business.route('/technician_chat/<chat_id>/update/<status>', methods=['GET'])
      def tech_company_business(chat_id, status):
       """
            endpoint which is used to update the status of the technician
            :params chat_id: chat_id, status: status
            :return: update the status of the technician
       """
    • @api_condominium_company_business.route('/<id_company>/condominium', methods=['GET'])
      def condominium_company_business(id_company):
      """
            endpoint which is used to have the condominium of a specific technician
            :params id_company: id_company
            :return: return the condominium of a specific technician
      """
    • @api_condominium_business.route('/<id_company>/number_condominium', methods=['GET'])
      def number_condominium_company_business(id_company):
      """
        endpoint which is used to have the number of condominium of a specific company
        :params id_company: id_company
        :return: return the number of condominium of a specific company
      """
    • @api_condominium_business.route('/number_condominium', methods=['GET'])
      def number_condominium_all_business():
      """
        endpoint which is used to have the number of condominium of a specific technician
        :params id_company: id_company
        :return: return the number of condominium of a specific technician
      """
    • @api_condominium_business.route('/condominium/<build_id>', methods=['GET'])
      def condominium_by_id(build_id):
      """
            endpoint which is used to have the condominium of a specific id
            :params id_company: id_company
            :return: return the number of condominium of a specific company
      """
    • @api_companies_business.route('/companies', methods=['GET'])
      def company_business():
      """
        endpoint which is used to have the name of all companies
        :params
        :return: return the name of all companies
      """
    • @api_calls_business.route('/companies/calls/<year>/<month>/<day>', methods=['GET'])
      def day_call_business(year, month, day):
      """
        endpoint which is used to have the call of a specif day for all companies
        :params year: year,  month: month, day: day
        :return: return the call of a specif day for all companies
      """
    • @api_calls_business.route('/<id_company>/calls/<year>/<month>/<day>', methods=['GET'])
      def day_call_company_business(id_company, year, month, day):
      """
        endpoint which is used to have the call of a specif day for a specific company
        :params id_company: id_company, year: year,  month: month, day: day
        :return: return the call of a specif day for a specific company
      """
    • @api_calls_business.route('/<id_company>/calls/<year>/<month>/<day>', methods=['GET'])
      def day_call_company_business(id_company, year, month, day):
      """
        endpoint which is used to have the call of a specif day for a specific company
        :params id_company: id_company, year: year,  month: month, day: day
        :return: return the call of a specif day for a specific company
      """
    • @api_call_status.route('/companies/calls/<status>', methods=['GET'])
      def day_call_business(status):
      """
        endpoint which is used to have the call of all companies for a specific status
        :params status: status
        :return: return the call of all companies for a specific status
      """
    • @api_call_status.route('/calls/<call_id>/update/<status>/<id_technician>', methods=['GET'])
      def day_call_company_business(call_id, status, id_technician):
      """
            endpoint which is used to update the id call and assigns the call of a specific technician
            :params call_id: call_id, status: status, id_technician: id_technician
            :return: update the id call and assigns the call of a specific technician
      """




ADAPTER SERVICE:

    • @api_geo_adapter.route('/geo_condominium_adapter', methods=['GET'])
      def geo_coder():
      """
            endpoint which is used to find the location of a specific condominium
            :params
            :return: find the location of a specific condominium
      """
