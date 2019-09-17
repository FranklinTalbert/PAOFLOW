# *************************************************************************************
# *                                                                                   *
# *   PAOFLOW *  Marco BUONGIORNO NARDELLI * University of North Texas 2016-2018      *
# *                                                                                   *
# *************************************************************************************
#
#  Copyright 2016-2018 - Marco BUONGIORNO NARDELLI (mbn@unt.edu) - AFLOW.ORG consortium
#
#  This file is part of AFLOW software.
#
#  AFLOW is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# *************************************************************************************

from PAOFLOW import PAOFLOW

def main():

  # Initialize PAOFLOW, indicating the name of the QE save directory.
  #   outputdir is named 'output' by default
  #   smearing is 'gauss' by default
  paoflow = PAOFLOW.PAOFLOW(savedir='silicon.save', outputdir='output_silicon', smearing='gauss', npool=1, verbose=True)
  paoflow.projectability()
  paoflow.pao_hamiltonian()

  # List the data keys
  paoflow.print_data_keys()

  # Calculate eigenvalues on the default ibrav=2 path
  paoflow.bands(ibrav=2, nk=2000)

  # Dimension of the grid is doubled by default
  #  e.g. 12x12x12 -> 24x24x24
  paoflow.interpolated_hamiltonian()

  # Calculate eigenvalues on the entire BZ grid
  paoflow.pao_eigh()

  paoflow.gradient_and_momenta()
  paoflow.adaptive_smearing()
  paoflow.dos(emin=-12., emax=2.2, ne=1000)
  paoflow.transport(emin=-12., emax=2.2, t_tensor=[[0,0]])
  paoflow.dielectric_tensor(emax=6., d_tensor=[[0,0]])
  paoflow.finish_execution()

if __name__== '__main__':
  main()

