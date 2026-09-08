def print_section(title):
    print(f"\n{"="*70}")
    print(title)
    print(f"{"="*70}")

print_section("User Auth System")
has_valid_password = True
acc_status = True
is_admin = False

print("Initial Security Section")
print(f"Valid Password provided: {has_valid_password}")
print(f"Account is Active: {acc_status}")
print(f"Is user Admin: {is_admin}")
print("\nPerforming initial checks...")

can_login = has_valid_password and acc_status
print(f"Can user login to the system: {can_login}")
print("\nChecking Admin Privilages...")
can_accsess_admin = can_login and is_admin
print(f"Can access Admin Panel: {can_accsess_admin}")

if __name__ == "__main__":
    print_section("User Auth System Completed")