from mdp.src.uc_mdp.mdp import *

class problem(object):
    def __init__(self, mdp_challenge, **kwargs):
        self.mdp_challenge=mdp_challenge
    def get_probability_nodes(self, S, Adjenc, A):
        transition = {}
        for wlt in range(0, np.size(Adjenc, 1)):
            allActions = A[S[wlt]]
            topSet = [(S[wlt], i) for i in allActions]
            vec = Adjenc[:, wlt]
            count = 0
            for tlw in range(0, len(vec)):
                if (vec[tlw]):
                    count += 1
            for qrt in range(0, np.size(topSet, 0)):
                prob = np.zeros(len(vec))
                prob[vec] = 1 / count
                act_type = (topSet[qrt][0], topSet[qrt][1])
                prob = prob / prob.sum()
                if (np.allclose(sum(prob), 1.0, rtol=1e-05, atol=1e-08)):
                    newdict = {act_type: prob}
                    transition.update(newdict)
                else:
                    None
        return transition
    def get_adjacency(self, A, S):
        am_nodes=len(S)
        new_A=np.eye(am_nodes, dtype=bool)
        for wlt in A:
            new_A[int(wlt[1])][int(wlt[0])] = True
        # test_symmetry=np.allclose(new_A, new_A.T, rtol=1e-05, atol=1e-08)
        # print('symmetry')
        # print(test_symmetry)
        return new_A

    def set_solver(self, params):
        S = self.mdp_challenge['S']
        P = self.mdp_challenge['P']
        A = self.mdp_challenge['A']
        Ad = self.mdp_challenge['Ad']
        Adjacenc = self.get_adjacency(Ad, S)
        T = self.get_probability_nodes(S, Adjacenc, A)
        self.obj_solver=mdp()
        self.obj_solver.set_gamma(params['gamma'])
        self.obj_solver.set_S(S)
        #self.obj_solver.set_adjacency_list(Ad)
        self.obj_solver.set_position_list(P)
        self.obj_solver.set_U()
        self.obj_solver.set_action(A)
        self.obj_solver.set_init_pi()
        self.obj_solver.set_T(T)
    def start_mdp_solver(self, rewards):
        R_dict = rewards
        self.obj_solver.set_R(R_dict)
        dict_mdp = self.obj_solver.start_mdp_algorithm()
        self.obj_solver.get_all_policy_options()
        return dict_mdp

if __name__ == '__main__':
    obj = problem()
    print(obj.obj_manifold.manifold)