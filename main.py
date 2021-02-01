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
    S = ['0', '1', '2', '3']
    Ad = [('0', '0'), ('0', '1'), ('1', '0'), ('1', '1'), ('1', '2'), ('2', '1'), ('2', '2'), ('2', '3'), ('3', '2'),
          ('3', '3'), ('3', '0'), ('0', '3')]
    P = [(-3, -3, 2), (3, -3, 2), (3, 3, 2), (0, 0, 2)]
    A = {'0': ['0', '1'], '1': ['1', '2'], '2': ['2', '3'], '3': ['3', '0']}
    R = {'2': 100}
    mdp_challenge = {'S': S, 'P': P, 'A': A, 'R': R, 'Ad': Ad}
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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
