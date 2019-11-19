import os,sys,inspect
import git
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from UpstreamTracker.MonitorChanges import parseMaintainers,sanitizeFileNames
import Constants.constants as cst

#git.Git("C:/Users/ABMARATH/Documents/Work/").clone("git://git.launchpad.net/~ubuntu-kernel/ubuntu/+source/linux/+git/bionic",branch = "master")
repo = git.Repo("~/PatchTracker/SUSE12")
latest_tags = sorted(repo.tags[:20], key=lambda t: t.commit.committed_date, reverse=True)
for t in repo.tags:
    print(t.commit.committed_date)


EMPTY_TREE_SHA   = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"

#parse maintainers file to get hyperV files
print("[Info] parsing maintainers files")
fileList = parseMaintainers(cst.PathToBionic)
print("[Info] Received HyperV file paths")
fileNames = sanitizeFileNames(fileList)

fifty_first_commits = list(repo.iter_commits('master',paths=fileNames))
print(len(fifty_first_commits))
#print(fifty_first_commits)

diff_list = []
last_commit = None
for commit in fifty_first_commits:
    if last_commit is not None:
        diff_list.append(commit.diff(last_commit))
    last_commit = commit

for diff_item in diff_list:
    print("A blob:\n{}".format(diff_item.a_blob.data_stream.read().decode('utf-8')))
    print("B blob:\n{}".format(diff_item.b_blob.data_stream.read().decode('utf-8'))) 