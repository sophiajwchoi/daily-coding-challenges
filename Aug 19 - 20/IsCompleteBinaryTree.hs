data Tree a = Leaf a | Node (Tree a) a (Tree a)
    deriving Show

complete :: Tree a -> Bool
complete (Leaf n) = True
complete (Node l _ r) = (size l == size r)
    where
        size (Leaf _) = 1
        size (Node l _ r) = size l + size r
