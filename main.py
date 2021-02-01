import logging
import argparse
from mdp.src.uc_mdp.uc_mdp_main import *

def test_mdp(params, mdp_challenge):
    obj_mdp = service_MDP()

    dict_mdp = obj_mdp.start_mdp(params, mdp_challenge)
    logging.info(dict_mdp['pi'])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ####################################################
    ### Challenge with Markov Decision Process (MDP) ###
    ####################################################

    # states
    S = ['0', '1', '2', '3']
    # Topology
    T = np.array([[True, True, True, True], [True, True, True, True], [True, True, True, True], [True, True, True, True]])
    # actions
    A = {'0': ['0', '1'], '1': ['1', '2'], '2': ['2', '3'], '3': ['3', '0']}
    # rewards
    R = {'2': 100}
    mdp_challenge = {'S': S, 'A': A, 'R': R, 'T': T}
    ##################
    ### Parameters ###
    ##################
    parser = argparse.ArgumentParser()
    parser.add_argument('--sample_time', '-Ts', type=float, help='Ts=0.1',
                        default='0.1', required=False)
    parser.add_argument('--gamma', '-gam', type=float, help='gamma=0.9',
                        default='0.9', required=False)
    args = parser.parse_args()
    params = vars(args)
    test_mdp(params, mdp_challenge)


