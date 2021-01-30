import os

# Working Of the app.
try:
	print("\n      Enter a Valid Directory to Organise.\n")
	org_dir = input(r"Directory:  ")
	all_files = os.listdir(org_dir)
	all_fext = []
	for f in all_files:
		_, fext = os.path.splitext(f)
		if fext not in all_fext:
			all_fext.append(fext)

	for ext in all_fext:
		if ext:
			os.mkdir(os.path.join(org_dir, ext))
	for f in all_files:
		_, ext = os.path.splitext(f)
		old_path = os.path.join(org_dir, f)
		new_path = os.path.join(org_dir, ext, f)
		os.rename(old_path, new_path)
	print(f"\n      Organised Files in {org_dir}")
except Exception as e:
	print(f"\n      Organisation Failed in '{org_dir}'")