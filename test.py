from git import Repo

repo = Repo('what the hell is this?')
assert not repo.bare

assert not repo.is_dirty()
print repo.untracked_files


