from git import Repo
repo = Repo('/Users/ray/Documents/Project/Conflict')
assert not repo.bare

assert not repo.is_dirty()
print repo.untracked_files


