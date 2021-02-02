from mdp.src.uc_mdp.uc_mdp_main import *
import argparse

'''
Start a MDP challenge
'''
def start_mdp(params, mdp_challenge):
    obj_mdp = service_MDP()
    dict_mdp = obj_mdp.start_mdp(params, mdp_challenge)
    logging.info(dict_mdp['pi'])
    return dict_mdp

'''
Get the points of a regular grid
'''
def get_meshgrid_points(params):
    xgrid = np.linspace(-10, 10, params["x_grid"])
    ygrid = np.linspace(-10, 10, params["y_grid"])
    X, Y=np.meshgrid(xgrid,ygrid)
    x=np.ravel(X)
    y=np.ravel(Y)
    z=0*y
    dict_pnts={}
    points=np.transpose(np.vstack((x, y, z))).tolist()
    for idx, act_point in enumerate(points):
        dict_pnts[str(idx)]=act_point
    return dict_pnts

"""


#states
S = ['0', '1', '2', '3']
#topology
T=np.array([[True, True, False, True],
                  [True, True, True, False],
                  [False, True, True, True],
                  [True, False, True, True]])"""

def get_simple_topology_for_regular_grid(params):
    amount_nodes=params["y_grid"]*params["x_grid"]
    S=[str(i) for i in range(0, amount_nodes)]
    T=np.ones((amount_nodes, amount_nodes), dtype=bool)
    return T, S