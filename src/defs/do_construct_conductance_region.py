def construct_conductance_regions(data_controller, left_data_controller, scatter_data_controller, right_data_controller=None):
    l_arry,l_attr = left_data_controller.data_dicts()
    s_arry,s_attr = scatter_data_controller.data_dicts()
    if right_data_controller != None:
        r_arry,r_attr = right_data_controller.data_dicts()
    arry,attr = self.data_controller.data_dicts()
    reset_arry,reset_attr = self.data_controller.data_dicts()