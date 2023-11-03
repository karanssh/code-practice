package main

import (
	"context"
	"fmt"
	"sync"

	"golang.org/x/sync/errgroup"
)

func main() {
	g, ctx := errgroup.WithContext(context.Background())

	var wg sync.WaitGroup
	for i := 0; i < 10; i++ {
		wg.Add(1)
		i := i
		g.Go(func() error {
			defer wg.Done()
			fmt.Printf("Task %d started\n", i)
			return nil
		})
	}

	go func() {
		wg.Wait()
		close(done)
	}()

	if err := g.Wait(); err != nil {
		fmt.Println("Error:", err)
	}
}
