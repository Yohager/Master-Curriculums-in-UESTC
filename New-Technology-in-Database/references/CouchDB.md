# CouchDB

## Architecture

CouchDB是一个面向文档的分布式NoSQL数据库，底层逻辑由Erlang实现，用Javascript作为查询语言基于HTTP进行交互，主要API风格为RESTful。数据通过JSON存储，存储结构为B-Tree，通过文档名(Doc-ID)或序列号查询。

由于存储的内容是文档式的，因此舍弃了关系型数据库的表结构而采用键对值的方式进行存储。这样每个数据都可以有自己特定的关键字以及值。

```bash
$ curl http://127.0.0.1:5984/wiki  # get information from wiki database
```

得到

```
{
  "db_name": "wiki",
  "doc_count": 0,
  "doc_del_count": 0,
  "update_seq": 0,
  "purge_seq": 0,
  "compact_running": false,
  "disk_size": 79,
  "instance_start_time": "1272453873691070",
  "disk_format_version": 5
}
```

实例来源[维基](https://en.wikipedia.org/wiki/Apache_CouchDB)。

## Eventual Consistency

由CAP定理，一个分布式系统最多在一致性，可行性，与分区容忍性中同时满足两个。CouchDB选择了可行性与分区容忍性，而通过最终一致性的技巧来弥补一致性上的缺陷。最终一致性使用户在访问数据库时能立刻返回本地的数据，并且各个分布式数据库之间通过通信来同步数据库的内容。为了处理由通信等带来的数据不一致问题，CouchDB采用MVCC对数据进行版本管理，使用户获得的每个数据都是某个版本下的，在之后通信恢复良好时处理数据库之间的冲突，并决定数据是否有效。同步的过程被称为增量复制([Incremental Replication](https://docs.couchdb.org/en/stable/intro/consistency.html))

# Fabric

Hyperledger是linux基金会下的一系列开源项目，Fabric就是其中之一，在区块链的发展中是3.0版本，常用于联盟链。Fabric是其中一个项目，用于基本的区块链部署，认证，交易执行。Fabric在新节点加入后会为其创造一个docker容器，并为其安装链码(chain code)作为其执行交易的方式。

## With CouchDB

Fabric将用户的数据存储为state，CouchDB作为一个NoSql数据库，提升了Fabric对数据存储的泛化性。每一个链码在执行时都代表了其自己的CouchDB数据库，其在执行链码时会广播到其他的节点，其他节点处理好相应的请求之后返回，最终使各个数据库的数据得到同步。这些节点可能扮演不同的角色，如银行，

