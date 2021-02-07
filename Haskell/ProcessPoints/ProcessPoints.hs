smallestDistances :: (RealFloat a) => [(a, a, a)] -> [a]  
smallestDistances cord = [dis |(l, w, h) <- cord, let dis = (l^2 + w^2 + h^2)**0.5, dis <= 10.0]

main = print(smallestDistances [(5,5,5), (3,4,5), (8,5,8), (9,1,4), (11,0,0), (12,13,14)])