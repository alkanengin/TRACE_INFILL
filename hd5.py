# Write the h5 file name
h5f_o = h5py.File(os.path.join(o_dir, outfile), 'w')
h5f_i = h5py.File(filename, 'r')

# Copy only attributes of Traces group
h5f_o.create_group('Traces')
[h5f_o['Traces'].attrs.create(key, val) for key,val in h5f_i['Traces'].attrs.items()]

# Copy header and scale information over
h5f_i.copy('Traces/TraceHeader', h5f_o['Traces'])
traces_i = get_traces(h5f_i)
scale = np.sqrt(np.var(traces_i.flatten()))
chunks = h5f_i['Traces/TraceData'].chunks

# Copy header information over
h5f_i.close()

# Write predictions
h5f_o.create_dataset('Traces/TraceData', dtype=np.float32, data=pred.T*scale, chunks=chunks)
h5f_o.close()
