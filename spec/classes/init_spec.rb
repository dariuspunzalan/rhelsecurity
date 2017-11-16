require 'spec_helper'
describe 'rhelsecurity' do
  context 'with default values for all parameters' do
    it { should contain_class('rhelsecurity') }
  end
end
