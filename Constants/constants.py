import platform
PATH_TO_REPOS = "../PatchTrackerRepos"
LINUX_REPO_NAME = "linux.git"
SECRET_REPO_NAME = "LSG-Secret"
MAINTAINERS_FILENAME = "MAINTAINERS"
PATH_TO_LAST_SHA = "../lastSHA"
UPSTREAM_TABLE_NAME = "Upstream-Dev"
DOWNSTREAM_TABLE_NAME = "DistributionPatches-Dev"

PathToSymbols = "../Symbols"
RedirectOp = '>>' if platform.system() == 'Windows' else '>'
