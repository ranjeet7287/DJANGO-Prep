# len/sum/min/max/sorted
s1={1,2,3,4,5}
s2={1,2,3,4,5,6,7,8}
print(len(s1))
print(sum(s1))
print(min(s1))
print(max(s1))
# sorted result in list
print(sorted(s1))

print(s1.union(s2))
print(s1.update(s2))
print(s1.intersection(s2))

# copy
s3=s2.copy(s2)
print(s3)