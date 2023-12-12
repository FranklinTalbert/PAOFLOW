def do_find_propogating_states( data_controller , region ):


    #If region == electrode only Im(k)=0 states are propogating

    if region == 'electrode':
        # z < 0 Psi = psi_j + sum_i(r_ij*psi_i)

        #z > L Psi = sum_i(t_ij*psi_i)

    if region == 'scattering':
        