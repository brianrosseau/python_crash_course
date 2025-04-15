visit = ['Montana', 'Italy', 'Hawaii', 'Banff', 'Israel']
print(visit)

sorted(visit) #The sorted() function arranges the alphabetically without permanently changing the original list.

print(visit)

sorted(visit, reverse=True)  # This does it in reverse alphbetical order (not permanent)

print(visit)

# Unlike the reverse() FUNCTION, the reverse() METHOD is PERMANENT. It must be run again to revert it back to the original.
visit.reverse()
print(visit)

visit.reverse()
print(visit)

# Use sort() method to arrange list alphabetically. It is PERMANENT.
visit.sort()
print(visit)

visit.sort(reverse=True)
print(visit)

print("My wife and I have", len(visit), "vacation sites we would like to visit.")