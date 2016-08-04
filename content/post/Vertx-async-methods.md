+++
date = "2016-08-04T22:02:37+08:00"
draft = false
title = "Vertx async methods"
tags = ["vertx","java","async"]
+++

I've been using [Vertx](http://vertx.io) for a while now, and so far it hasn't disappointed me.  There's one thing though, because Vertx came out before Java 8, it doesn't use `java.util.concurrent.CompletableFuture`.  Instead, it rolls its own future/promise implementation called `io.vertx.core.Future`.

There was a [thread](https://groups.google.com/forum/?fromgroups#!topic/vertx/KbaXI1ULGYY) on the Vertx discussion group a few days ago, I wrote about what I knew.  Here's a copy.

> I've noticed that `CompletableFuture` sometimes assigns my HttpClient instance to run on another thread, which leads to a Vertx warning.  It's "fixable" by wrapping a HttpClient call with a `vertx.runOnContext()`, but I *guess* the more idiomatic way would be to avoid using `CompletableFuture`, as it's a different thread handling implementation to the one in Vertx.

> `CompletableFuture`, according to Java documents, uses JVM's default fork/join pool.  Although one interesting thing I've observed is that HttpClient calls chained with `CompletableFuture` tends to run on Vertx's own threads as well (with thread names like vert.x-eventloop-thread-X).  This is confusing, to me at least, maybe someone in the know could chime in?

> To stay on topic, the default `io.vertx.core.Future` already has support for a `.all` operation, see http://vertx.io/docs/vertx-core/java/#_async_coordination.
If that's not enough for your use case, I've been using this implementation https://github.com/jtruelove/vertx-util with no problems.

There's too much code that depend on `CompletableFuture` in my company's backend server now, going back to change them to use`io.vertx.core.Future` is a time-consuming venture that may not even make a difference.  I will be using vertx-util to chain my futures from now on though.
