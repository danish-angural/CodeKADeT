export var files = [
    {
      name: 'material2',
      type: 'folder',
      children: [
        {
          name: 'src',
          type: 'folder',
          children: [
            {
              name: 'cdk',
              type: 'folder',
              children: [
                { name: 'package.json', type: 'file', children: []},
                { name: 'BUILD.bazel', type: 'file', children: []},
              ]
            },
            { name: 'lib', type: 'folder' }
          ]
        }
      ]
    },
    {
      name: 'angular',
      type: 'folder',
      children: [
        {
          name: 'packages',
          type: 'folder',
          children: [
            { name: '.travis.yml', type: 'file' },
            { name: 'firebase.json', type: 'file' }
          ]
        },
        { name: 'package.json', type: 'file' }
      ]
    },
    {
      name: 'angularjs',
      type: 'folder',
      children: [
        { name: 'gulpfile.js', type: 'file' },
        { name: 'README.md', type: 'file' }
      ]
    }
  ];
  