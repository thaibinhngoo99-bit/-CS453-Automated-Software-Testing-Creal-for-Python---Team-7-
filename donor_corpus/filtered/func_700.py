def cross(policy1, policy2):
    newPolicy = policy1.copy()
    mask = np.random.randint(2, size=newPolicy.shape).astype(np.bool)
    newPolicy[mask] = policy2[mask]
    return newPolicy