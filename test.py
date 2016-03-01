import git

repo = Repo('This is a repository!!!')
assert not repo.bare

assert not repo.is_dirty()
print repo.untracked_files


