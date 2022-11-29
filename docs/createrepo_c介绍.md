# createrepo_c介绍

一句话概括：

**createrepo_c 用于创建/管理 yum repository元数据 （repodata）**


## createrepo基本信息

```
Installed Packages
Name         : createrepo_c
Version      : 0.17.7
Release      : 6.el8
Architecture : x86_64
Size         : 189 k
Source       : createrepo_c-0.17.7-6.el8.src.rpm
Repository   : @System
From repo    : appstream
Summary      : Creates a common metadata repository
URL          : https://github.com/rpm-software-management/createrepo_c
License      : GPLv2+
Description  : C implementation of Createrepo.
             : A set of utilities (createrepo_c, mergerepo_c, modifyrepo_c)
             : for generating a common metadata repository from a directory of
             : rpm packages and maintaining it.
```



```
# rpm -ql createrepo_c
/usr/bin/createrepo
/usr/bin/createrepo_c
/usr/bin/mergerepo
/usr/bin/mergerepo_c
/usr/bin/modifyrepo
/usr/bin/modifyrepo_c
/usr/bin/sqliterepo_c
/usr/lib/.build-id
/usr/lib/.build-id/07
/usr/lib/.build-id/07/d49fe8aca16727eacb8ab41b18ecf599d3679e
/usr/lib/.build-id/23
/usr/lib/.build-id/23/06f9f5f49a1183ad3ac9c1fabbee4642ff4921
/usr/lib/.build-id/97
/usr/lib/.build-id/97/8040c63ed4bf2cfd673212eb6426bc5c70d576
/usr/lib/.build-id/cf
/usr/lib/.build-id/cf/1315cbf5f0796f5146bd13240444afa65e440d
/usr/share/bash-completion/completions/createrepo_c
/usr/share/bash-completion/completions/mergerepo_c
/usr/share/bash-completion/completions/modifyrepo_c
/usr/share/bash-completion/completions/sqliterepo_c
/usr/share/doc/createrepo_c
/usr/share/doc/createrepo_c/README.md
/usr/share/man/man8/createrepo_c.8.gz
/usr/share/man/man8/mergerepo_c.8.gz
/usr/share/man/man8/modifyrepo_c.8.gz
/usr/share/man/man8/sqliterepo_c.8.gz
```
