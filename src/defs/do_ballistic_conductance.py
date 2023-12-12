def find_eigenchannels( energy, bands):
    import numpy as np
    eigenchannels = np.array([])
    for E in energy:
        for band in bands:
            
    return


def do_ballistic_conductance( left_data_controller, scatter_data_controller, right_data_controller = None, energies=[]):
    import numpy as np
    l_arry,l_attr = left_data_controller.data_dicts()
    s_arry,s_attr = scatter_data_controller.data_dicts()
    # if right_data_controller is not None:
    #     r_arry,r_attr = right_data_controller.data_dicts()
    print('\n+++++++++++++++\n',l_arry["E_k"][600,:,:],'\n+++++++++++++++\n')
    print('\n++++++++++++++++',s_arry.keys(),'\n++++++++++++++++++++++')
    find_eigenchannels(energies, l_arry['E_k'])

    
    #find channels
    #Assumes wire in z direction

    #Take Complex Band Structure of leads
    
    #Find rightward propogating states

    #Orthogonalize using Eq 23
        #Depends on partial/partial z of psi

    #In left lead find t_ij for rightward states

    #Find Bold(T) = matrix T_ij = sqrt(I_i/I_j)t_ij

    #Find T using Eq 19 T = Tr(Bold(T^+)Bold(T))

    #Contribution per eigenchannel T_i = eigenvalues of Bold(T^+)Bold(T)

    #Conductance G = G_0*sum(T_i)