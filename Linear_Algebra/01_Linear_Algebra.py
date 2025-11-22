'''
Q1. What does it mean for a matrix A to have an inverse?
Ans:
A matrix A has an inverse A⁻¹ if it is nonsingular.
Their product gives the identity matrix: A * A⁻¹ = I.
'''
# Example:
# A = [[1, 2],
#      [3, 4]]

# • Step 1: Compute determinant  
#   det(A) = (1*4) − (2*3) = −2  
#   (non-zero → inverse exists)

# • Step 2: Use 2×2 inverse formula  
#   A⁻¹ = (1/det) * [[ d, −b ],
#                    [−c,  a ]]

# • Step 3: Substitute values  
#   A⁻¹ = (1/−2) * [[ 4, −2 ],
#                   [−3,  1 ]]

# • Step 4: Meaning  
#   A * A⁻¹ = I (identity matrix)



'''
Q2. What does it mean when Aᵏ = I? (Matrix order)
Ans:
If Aᵏ = I for some smallest positive integer k,
we say “A has order k”.
It means A repeats itself every k powers.
'''
# Let A be a matrix such that A⁴ = I.

# • Smallest such power is 4 → order of A is 4.
# • Then powers start repeating:
#     A⁵ = A
#     A⁶ = A²
#     A⁷ = A³
#     A⁸ = I  (cycle completes)



'''
Q3. How do we simplify high powers like Aⁿ when Aᵐ = I?
Ans:
We reduce the exponent using modulo:
Aⁿ = A^(n mod m)

This works because powers cycle every m steps.
'''
# Example:
# If A⁴ = I, then A⁹ = A^(9 mod 4) = A¹.

# See again,
# Given A⁴ = I:
# • Compute 9 mod 4 → remainder = 1
# • So, A⁹ = A¹
# Therefore: A⁹ = A



'''
Q4. What is the determinant rule for matrix powers?
Ans:
det(Aᵏ) = (det A)ᵏ.
This makes finding determinants of large powers easy.
'''
# Suppose det(A) = 3.

# We want det(A⁵).

# • Step 1: Use the rule  
#   det(A⁵) = (det A)⁵

# • Step 2: Substitute det(A) = 3  
#   det(A⁵) = 3⁵

# • Step 3: Evaluate 3⁵  
#   3⁵ = 3 × 3 × 3 × 3 × 3 = 243

# Final Answer: det(A⁵) = 243



'''
Visualising Determinant:
# Visual meaning of determinant

• Think of a matrix as a machine acting on a rubber sheet.

• det = 1  → sheet keeps same area (only rotated/skewed).

• det > 1  → sheet is stretched (area increases).

• 0 < det < 1  → sheet is shrunk (area decreases).

• det = 0  → sheet is crushed into a line/point (no area left).
              → cannot “un-crush” → no inverse.

• det < 0  → sheet is flipped (mirror reflection) plus stretched/shrunk.

# In short:
# determinant = how much the matrix stretches/shrinks/flips space.
'''



'''
Q5. Why does det(0 matrix) = 0?
Ans:
Because the zero matrix collapses all space to a point,
so its determinant (area/volume scaling) becomes zero.
'''
# Example:
# Any matrix with all rows 0 must have determinant = 0.
# ...........................................................
# • If every row is 0, the matrix gives no stretching at all.
# • It sends every vector to 0 → complete collapse.
# • Therefore: det = 0.



'''
Q6. What key trick helps when A² relates to A⁻¹ in equations?
Ans:
Try multiplying by A or A⁻¹ to form the identity.
This often converts the equation into something usable,
like reducing powers or finding relationships.
'''
# Given: A² = A⁻¹

# • Multiply both sides by A:
#   A² · A = A⁻¹ · A

# • This gives:
#   A³ = I

# So the matrix has order 3.


'''
Q7. How can we use A³ = I to simplify A¹⁰?
Ans:
Since A³ = I, reduce the exponent:
A¹⁰ = A^(10 mod 3) = A¹.
'''
# Example:
# 10 mod 3 = 1 → A¹.
# ..................
# 10 mod 3 = 1
# So, A¹⁰ = A¹ = A.


